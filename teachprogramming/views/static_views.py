#from pyramid.view      import view_config
from pyramid.renderers import render_to_response

from . import web, etag
from teachprogramming.lib.misc import funcname


def render_static_mako_from_caller(request):
    return render_to_response(
        'teachprogramming:templates/html/static/{0}.mako'.format(funcname(level=2)),
        request.matchdict,
        request=request,
    )

@etag
@web
def home(request):
    return render_static_mako_from_caller(request)

@etag
@web
def activities(request):
    return render_static_mako_from_caller(request)

@etag
@web
def reference(request):
    return render_static_mako_from_caller(request)

@etag
@web
def contact(request):
    return render_static_mako_from_caller(request)

@etag
@web
def projects(request):
    return render_static_mako_from_caller(request)

@etag
@web
def units(request):
    return render_static_mako_from_caller(request)
