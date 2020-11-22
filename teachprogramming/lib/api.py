import os
import logging
from pathlib import Path
from typing import NamedTuple

import falcon

log = logging.getLogger(__name__)


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


class FileWrapper():
    def __init__(self, f):
        self.f = f
        self.p = Path(f.path)
    @property
    def project(self):
        return self.p.stem


class FileCollection():
    def __init__(self, path):
        self.path = path
        self.files = tuple(Path(f.path) for f in fast_scan(path))
    @property
    def file_list(self):
        return tuple(str(f.relative_to(self.path)) for f in self.files)


# Request Handler --------------------------------------------------------------

class IndexResource():
    def __init__(self, path):
        #self.path = path
        self.files = FileCollection(path)
    def on_get(self, request, response):
        response.media = {
            'version': 'test',
            'files': self.files.file_list,
        }
        response.status = falcon.HTTP_200

# Setup App -------------------------------------------------------------------

def create_wsgi_app(path=None, **kwargs):
    app = falcon.API()
    app.add_route(r'/', IndexResource(path))
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
        log.info('start')
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass