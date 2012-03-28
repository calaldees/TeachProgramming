from pyramid.view import view_config
from pyramid.renderers import render_to_response
from pyramid.response import Response

from ..models import (
    DBSession,
    MyModel,
    )

import teachprogramming.lib.make_ver  as make_ver
import teachprogramming.lib.constants as constants


@view_config(route_name='home', renderer='teachprogramming:templates/home.mako')
def home(request):
    return {}

@view_config(route_name='project_doc')
def project_doc(request):
    return render_to_response(
        'teachprogramming:templates/projects/%s.mako' % request.matchdict['project'], 
        {'project':request.matchdict['project'], 
         'format' :request.matchdict['format' ],},
        request=request,
    )

@view_config(route_name='project_code')
def project_code(request):
    code = '\n'.join( make_ver.make_ver(constants.project_filename_dict % request.matchdict, request.matchdict.get('version')) )
    response = Response(code)
    response.headers['Content-type'] = "text/plain; charset=utf-8"
    return response



# Old reference

#@view_config(route_name='home', renderer='myproject:templates/mytemplate.pt')
#def my_view(request):
#    one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
#    return {'one':one, 'project':'MyProject'}

#@view_config(route_name='hello_world')
#def hello_world(request):
#    from pyramid.response import Response
#    return Response('Hello world!')
    
#@view_config(route_name='mako_test', renderer='mako_test.mako')
#def mako_test(request):
#    #from pyramid.renderers import render_to_response
#    #return render_to_response('myproject:templates/mako_test.mako',
#    #                          {'foo':1, 'bar':2, 'project':'my project',},
#    #                          request=request)
#    d = {'project':'my project'}
#    d.update(request.matchdict)
#    return d
