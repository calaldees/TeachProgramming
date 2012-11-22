#from pyramid.view      import view_config
from pyramid.renderers import render_to_response

from teachprogramming.lib.web import etag, get_setting


import inspect
def render_static_mako_from_caller(request):
    calling_method_name = inspect.stack()[1][3]
    return render_to_response(
        'teachprogramming:templates/html/static/{0}.mako'.format(calling_method_name),
        {},
        request=request,
    )

#@view_config(route_name='home', renderer='teachprogramming:templates/home.mako')
@etag
def home(request):
    return render_static_mako_from_caller(request)
    #return {}

@etag
def activities(request):
    return render_static_mako_from_caller(request)

@etag
def reference(request):
    return render_static_mako_from_caller(request)

@etag
def contact(request):
    return render_static_mako_from_caller(request)

@etag
def projects(request):
    return render_static_mako_from_caller(request)
