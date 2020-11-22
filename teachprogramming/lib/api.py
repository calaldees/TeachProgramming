import os
import re
import logging
from pathlib import Path
from typing import NamedTuple
from functools import cached_property

import falcon

import _falcon_helpers
from make_ver2 import ProjectVersions

log = logging.getLogger(__name__)


# Fastscan

def _default_exclude_filter(f):
    if f.name.startswith('.') or f.name.startswith('_'):
        return True
    if f.name == 'cgi-bin':
        return True
def _default_select_filter(f):
    #if f.name.endswith('.ver'):
    return True
def fast_scan(root, path=None, exclude_filter=_default_exclude_filter, select_filter=_default_select_filter):
    path = path or ''
    for f in os.scandir(os.path.join(root, path)):
        if exclude_filter(f):
            continue
        if f.is_file() and select_filter(f):
            yield f
        if f.is_dir():
            yield from fast_scan(root, os.path.join(path, f.name), exclude_filter=exclude_filter, select_filter=select_filter)

class FileCollection():
    def __init__(self, path):
        self.path = path
        self.files = tuple(Path(f.path) for f in fast_scan(path))
    #@cached_property
    #def file_list(self):
    #    return tuple(str(f.relative_to(self.path)) for f in self.files)
    @cached_property
    def projects(self):
        return {str(f.relative_to(self.path)).replace('.ver','') for f in self.files if f.suffix == '.ver'}
    def project_files(self, project):
        return {str(f) for f in self.files if project+'.' in str(f)}


# Request Handler --------------------------------------------------------------

class IndexResource():
    def on_get(self, request, response):
        response.media = {
            'hello': 'world',
        }
        response.status = falcon.HTTP_200

class ProjectResource():
    def __init__(self, path):
        self.files = FileCollection(path)
    def on_index(self, request, response):
        response.media = {'projects': self.files.projects}
        response.status = falcon.HTTP_200
    def on_get(self, request, response, path):
        pv = ProjectVersions(self.files.project_files(path))
        response.media = {
            'versions': pv.versions,
            'languages': pv.data,
        }
        response.status = falcon.HTTP_200

# Setup App -------------------------------------------------------------------

def create_wsgi_app(path=None, **kwargs):
    app = falcon.API()
    app.add_route(r'/', IndexResource())
    _falcon_helpers.add_sink(app, 'project', ProjectResource(path), func_path_normalizer=_falcon_helpers.func_path_normalizer_no_extension)
    _falcon_helpers.update_json_handlers(app)
    return app

# Commandlin Args -------------------------------------------------------------

def get_args():
    import argparse

    parser = argparse.ArgumentParser(
        prog=__name__,
        description='''
            Provide a URL endpoint to return metadata of media
        ''',
    )

    parser.add_argument('path', action='store', default='./', help='')

    parser.add_argument('--host', action='store', default='0.0.0.0', help='')
    parser.add_argument('--port', action='store', default=8000, type=int, help='')

    parser.add_argument('--log_level', action='store', type=int, help='loglevel of output to stdout', default=logging.INFO)

    kwargs = vars(parser.parse_args())
    return kwargs

# Main ------------------------------------------------------------------------

if __name__ == '__main__':
    kwargs = get_args()

    logging.basicConfig(level=kwargs['log_level'])

    from wsgiref import simple_server
    httpd = simple_server.make_server(kwargs['host'], kwargs['port'], create_wsgi_app(**kwargs))
    try:
        log.info(f'start {kwargs}')
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass