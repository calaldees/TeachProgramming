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

def etag(etag_render_func):
    def etag(f, *args, **kwargs):
        request = request_from_args(args)
        
        etag_enabled = get_setting('server.etag_enabled', request, return_type=bool)
        
        if (etag_enabled):
            if etag_render_func:
                etag = etag_render_func(request)
            else:
                etag = "%s %s" % (target.__name__, str(request.params) )
            if etag and etag in request.if_none_match:
                log.debug('etag matched - aborting render - %s' % etag)
                raise exception_response(304)
        
        result = f(*args, **kwargs) # Execute the wrapped function
        
        if (etag_enabled):
            log.debug('etag set - %s' % etag)
            result.etag = etag
            
        return result
    return decorator(etag)

#@decorator
#def etag(target, *args, **kwargs):
#    """
#    Pyramid has no etag decorator .. WTF!!!! ..
#    this is my first revision - needs params, but it works for the one case im using it for at the moment
#    """
#    assert isinstance(args[0], pyramid.request.Request)
#    request = args[0]
#    
#    etag_enabled = get_setting('etag_enabled', request, return_type=bool)
#    if (etag_enabled):
#        etag = "%s %s %s" % (target.__name__, str(request.matchdict), str(normalize_datetime(datetime.datetime.now(), get_setting('etag_expire',request))) )
#        log.debug('etag matched - aborting render - %s' % etag)
#        if etag in request.if_none_match:
#            raise exception_response(304)
#    
#    result = target(*args, **kwargs) # Execute the wrapped function
#    
#    if (etag_enabled):
#        log.debug('etag set - %s' % etag)
#        result.etag = etag
#        
#    return result

