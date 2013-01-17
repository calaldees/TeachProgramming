from decorator import decorator

import pyramid.request
import pyramid.registry
from pyramid.settings import asbool
from pyramid.httpexceptions import exception_response

from teachprogramming.lib.misc import normalize_datetime, funcname


import logging
log = logging.getLogger(__name__)



def get_setting(key, request=None, return_type=None):
    if request:
        value = request.registry.settings.get(key)
    else:
        value = pyramid.registry.global_registry.settings.get(key)
    if return_type=='bool' or return_type==bool:
        value = asbool(value)
    if return_type=='int' or return_type==int:
        value = int(value)
    return value

def request_from_args(args):
    # Extract request object from args
    request = None
    for arg in args:
        if isinstance(arg, pyramid.request.Request):
            request = arg
            break
    assert request
    return request


def _etag_render_func_default(request):
    return "-".join([
        request.path_qs,
        normalize_datetime(accuracy=get_setting('server.etag_expire', request)).ctime(), # use epoc here instead
        # request.POST ??,
        # request.session_id ??,
    ])

def etag(etag_render_func=_etag_render_func_default):
    """
    eTag decorator
    
    use:
    
    @etag()
    def my_route_view(request):
        pass
    
    by default this will use the request.route_qs + expire time as the etag
    
    You can specify a function to generate an etag string, this is passed the single argument 'request'
    
    @etag(lambda request: request.path_qs)
    def my_route_view(request):
        pass
    
    """
    def etag(f, *args, **kwargs):
        request = request_from_args(args)
        
        etag_enabled = get_setting('server.etag_enabled', request, return_type=bool)
        
        if etag_enabled:
            etag = etag_render_func(request)
            if etag and etag in request.if_none_match:
                log.debug('etag matched - aborting render - %s' % etag)
                raise exception_response(304)
        
        result = f(*args, **kwargs) # Execute the wrapped function
        
        if etag_enabled:
            log.debug('etag set - %s' % etag)
            result.etag = etag
        
        return result
    return decorator(etag)
