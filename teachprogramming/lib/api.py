import logging
from pathlib import Path
from typing import Iterable

import falcon

import _falcon_helpers
from make_ver2 import ProjectVersions, LanguageVersions, LANGUAGES

log = logging.getLogger(__name__)


LANGUAGE_EXTENSIONS = frozenset((*LANGUAGES.keys(), *('ver.json',)))

class FileCollection():
    @staticmethod
    def walk_language_files(path: Path):  #  -> Generator[Path]
        def _exclude_dir(dir: str):
            return any((
                dir.startswith('_'),
                dir.startswith('cgi'),
                dir.startswith('.'),
                dir in ('bin', 'obj'),
            ))
        for root, dirs, files in path.walk():
            dirs = filter(_exclude_dir, dirs)
            for file in map(root.joinpath, files):
                if ''.join(file.suffixes).strip('.') in LANGUAGE_EXTENSIONS:
                    yield file

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.files = tuple(self.walk_language_files(self.path))

# Request Handler --------------------------------------------------------------

class IndexResource():
    def on_get(self, request, response):
        raise falcon.HTTPFound('/static/index.html')

class LanguageReferenceResource():
    def __init__(self, path: str | Path):
        self.lv = LanguageVersions(FileCollection(path).files)
    def on_get(self, request, response):
        response.media = {
            'versions': self.lv.all_versions,
            'languages': self.lv.languages,
        }
        response.status = falcon.HTTP_200

class ProjectListResource():
    def __init__(self, path: str | Path):
        self.project_names = tuple(
            str(f.relative_to(path)).replace('.ver.json','')
            for f in FileCollection(path).files
            if ''.join(f.suffixes) in {'.ver.json',}
        )
    def on_get(self, request, response):
        response.media = {'projects': self.project_names}
        response.status = falcon.HTTP_200

class ProjectResource():
    def __init__(self, path: str | Path):
        self.file_collection = FileCollection(path)
    #def on_index(self, request, response):
    #    response.media = {'projects': self.files.projects}
    #    response.status = falcon.HTTP_200
    def on_get(self, request, response, project_name: str):
        pv = ProjectVersions(self.project_files(project_name))
        response.media = {
            'versions': {'paths': pv.versions.paths, 'parents': pv.versions.parents},
            'languages': pv.languages,
            'diffs': pv.diffs,
        }
        response.status = falcon.HTTP_200
    def project_files(self, project_name: str) -> Iterable[Path]:
        def _filter_file(f):
            relative_path = f.relative_to(self.file_collection.path)
            return project_name == str(relative_path.parent.joinpath(relative_path.name.removesuffix(''.join(f.suffixes))))
        return tuple(filter(_filter_file, self.file_collection.files))


# Setup App -------------------------------------------------------------------

def create_wsgi_app(project_path=None, language_path=None, **kwargs):
    app = falcon.App()
    app.add_route(r'/', IndexResource())
    app.add_static_route(r'/static', str(Path('static').resolve()))
    app.add_route(r'/api/v1/language_reference.json', LanguageReferenceResource(language_path))
    app.add_route(r'/api/v1/projects.json', ProjectListResource(project_path))
    _falcon_helpers.add_sink(app, r'/api/v1/projects/', ProjectResource(project_path), func_path_normalizer=_falcon_helpers.func_path_normalizer_no_extension)
    _falcon_helpers.update_json_handlers(app)
    # TODO: Currently unable to drop into debugger on error - investigate?
    # https://falcon.readthedocs.io/en/stable/api/app.html#falcon.App.add_error_handler
    # add_error_handler(exception, handler=None)
    return app

# Export ----------------------------------------------------------------------

def export():
    from falcon import testing
    test_client = testing.TestClient(app)
    def read_write(url):
        log.info(url)
        path = Path(url.strip('/'))
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('wt', encoding="utf-8") as filehandle:
            data = test_client.simulate_get(url)
            filehandle.write(data.text)
            return data.json
    read_write('/api/v1/language_reference.json')
    projects = read_write('/api/v1/projects.json')['projects']
    for project in projects:
        read_write(f'/api/v1/projects/{project}.json')


# Commandlin Args -------------------------------------------------------------

def get_args():
    import argparse

    parser = argparse.ArgumentParser(
        prog=__name__,
        description='''
            Provide a URL endpoint to return metadata of media
        ''',
    )

    parser.add_argument('project_path', action='store', default='./', help='')
    parser.add_argument('language_path', action='store', default='./', help='')

    parser.add_argument('--host', action='store', default='0.0.0.0', help='')
    parser.add_argument('--port', action='store', default=8000, type=int, help='')

    parser.add_argument('--export', action='store_true')

    parser.add_argument('--log_level', action='store', type=int, help='loglevel of output to stdout', default=logging.INFO)

    kwargs = vars(parser.parse_args())
    return kwargs

# Main ------------------------------------------------------------------------

if __name__ == '__main__':
    kwargs = get_args()

    logging.basicConfig(level=kwargs['log_level'])

    from wsgiref import simple_server
    app = create_wsgi_app(**kwargs)

    if kwargs['export']:
        export()
        exit()

    try:
        log.info(f'start {kwargs}')
        httpd = simple_server.make_server(kwargs['host'], kwargs['port'], app)
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass