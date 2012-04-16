from pyramid.settings import asbool
from pyramid.request import Request
from pyramid.response import Response
from pyramid.httpexceptions import exception_response

from teachprogramming.lib.misc import normalize_datetime, funcname

from decorator import decorator
import datetime

import logging
log = logging.getLogger(__name__)

def get_setting(request, key, bool=False):
    value = request.registry.settings.get(key) #get_current_registry().settings.get('beaker.cache.enabled')
    if bool:
        value = asbool(value)
    return value

@decorator
def etag(target, *args, **kwargs):
    """
    Pyramid has no etag decorator .. WTF!!!! ..
    this is my first revision - needs params, but it works for the one case im using it for at the moment
    """
    assert isinstance(args[0], Request)
    request = args[0]

    etag_enabled = get_setting(request, 'etag_enabled', bool=True)
    if (etag_enabled):
        etag = "%s %s %s" % (target.__name__, str(request.matchdict), str(normalize_datetime(datetime.datetime.now(), get_setting(request, 'etag_expire'))) )
        log.debug('etag matched - aborting render - %s' % etag)
        if etag in request.if_none_match:
            raise exception_response(304)
    
    result = target(*args, **kwargs) # Execute the wrapped function
    
    if (etag_enabled):
        log.debug('etag set - %s' % etag)
        result.etag = etag
        
    return result
