import os
import re
from pathlib import Path
from functools import partial
import json
from types import MappingProxyType

from falcon import media


def func_path_normalizer(path):
    return str(path)
def add_sink(app, prefix, resource, func_path_normalizer=func_path_normalizer):
    def _sink(request, response):
        path = func_path_normalizer(Path(re.sub(f'^/{prefix}/', '', request.path)))
        if not path:
            return resource.on_index(request, response)
        return getattr(resource, f'on_{request.method.lower()}')(request, response, path)
    app.add_sink(_sink, prefix=f'/{prefix}/')

def func_path_normalizer_no_extension(path):
    return os.path.join(str(path.parent), path.stem).strip('./')


def update_json_handlers(app):
    def _json_dumps(obj):
        if isinstance(obj, (dict, MappingProxyType)):
            return dict(obj)
        if isinstance(obj, set):
            return tuple(obj)
        return obj
    media_handlers = {
        'application/json': media.JSONHandler(
            dumps=partial(json.dumps, default=_json_dumps),
            loads=json.loads,
        ),
    }
    app.req_options.media_handlers.update(media_handlers)
    app.resp_options.media_handlers.update(media_handlers)
