import logging
from pathlib import Path
from functools import cached_property
from typing import Iterable, Generator

import falcon

import _falcon_helpers
from make_ver2 import ProjectVersions, LanguageVersions, LANGUAGES

log = logging.getLogger(__name__)


LANGUAGE_EXTENSIONS = frozenset((*LANGUAGES.keys(), *('ver',)))

class FileCollection():
    @staticmethod
    def walk_language_files(path: Path):  #  -> Generator[Path]
        def _exclude_dir(dir: str):
            return any((
                dir.startswith('_'),
                dir.startswith('cgi'),
                dir.startswith('.'),
            ))
        for root, dirs, files in path.walk():
            dirs = filter(_exclude_dir, dirs)
            for file in map(root.joinpath, files):
                if file.suffix.strip('.') in LANGUAGE_EXTENSIONS:
                    yield file

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.files = tuple(self.walk_language_files(self.path))
    @cached_property
    def project_names(self) -> Iterable[str]:
        return {
            str(f.relative_to(self.path)).replace('.ver','')
            for f in self.files
            if f.suffix == '.ver'
        }
    def project_files(self, project_name: str) -> Iterable[Path]:
        return {f for f in self.files if project_name == f.stem}


# Request Handler --------------------------------------------------------------

class IndexResource():
    def on_get(self, request, response):
        raise falcon.HTTPFound('/static/index.html')

class LanguageReferenceResource():
    def __init__(self, path: str | Path):
        self.files = FileCollection(path).files
        self.lv = LanguageVersions(self.files)
    def on_get(self, request, response):        
        response.media = {
            'versions': self.lv.all_versions,
            'languages': self.lv.languages,
        }
        response.status = falcon.HTTP_200

class ProjectListResource():
    def __init__(self, path: str | Path):
        self.project_names = FileCollection(path).project_names
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
        pv = ProjectVersions(self.file_collection.project_files(project_name))
        response.media = {
            'versions': pv.versions,
            'languages': pv.data,
        }
        response.status = falcon.HTTP_200

# Setup App -------------------------------------------------------------------

def create_wsgi_app(project_path=None, language_path=None, **kwargs):
    app = falcon.API()
    app.add_route(r'/', IndexResource())
    app.add_static_route(r'/static', str(Path('static').resolve()))
    app.add_route(r'/api/v1/language_reference.json', LanguageReferenceResource(language_path))
    app.add_route(r'/api/v1/projects.json', ProjectListResource(project_path))
    _falcon_helpers.add_sink(app, r'/api/v1/projects/', ProjectResource(project_path), func_path_normalizer=_falcon_helpers.func_path_normalizer_no_extension)
    _falcon_helpers.update_json_handlers(app)
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