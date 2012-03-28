from pyramid.view import view_config
from pyramid.renderers import render_to_response

from ..models import (
    DBSession,
    MyModel,
    )

#@view_config(route_name='home', renderer='myproject:templates/mytemplate.pt')
#def my_view(request):
#    one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
#    return {'one':one, 'project':'MyProject'}

@view_config(route_name='home', renderer='myproject:templates/home.mako')
def home(request):
    return {}

@view_config(route_name='hello_world')
def hello_world(request):
    from pyramid.response import Response
    return Response('Hello world!')
    
@view_config(route_name='mako_test', renderer='mako_test.mako')
def mako_test(request):
    #from pyramid.renderers import render_to_response
    #return render_to_response('myproject:templates/mako_test.mako',
    #                          {'foo':1, 'bar':2, 'project':'my project',},
    #                          request=request)
    d = {'project':'my project'}
    d.update(request.matchdict)
    return d

@view_config(route_name='project')
def project(request):
    return render_to_response(
        'myproject:templates/projects/%s.mako' % request.matchdict['project'], 
        {'project':request.matchdict['project'], 
         'format' :request.matchdict['format' ],},
        request=request,
    )
