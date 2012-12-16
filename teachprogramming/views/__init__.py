from decorator import decorator
from ..lib.pyramid_helpers import request_from_args, get_setting, etag

__all__ = [
    'base','web','etag'
]


#-------------------------------------------------------------------------------
# Global Variables
#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
# Base - executed on all calls
#-------------------------------------------------------------------------------
@decorator
def base(target, *args, **kwargs):
    """
    The base instructions to be executed for most calls
    """
    request = request_from_args(args)
    
    default_language = get_setting('default_language', request)
    if 'selected_lang' not in request.matchdict:
        request.matchdict['selected_lang'] = request.session.get('selected_lang'  ,default_language)
    if request.matchdict.get('selected_lang') != request.session.get('selected_lang'):
        request.session  ['selected_lang'] = request.matchdict.get('selected_lang',default_language)
    
    result = target(*args, **kwargs)
    
    # Enable Pyramid GZip on all responses - NOTE! In a production this should be handled by nginx for performance!
    if get_setting('server.gzip', request, return_type=bool):
        request.response.encode_content(encoding='gzip', lazy=False)
    
    return result


#-------------------------------------------------------------------------------
# eTag override (until it can be implemented fully)
#-------------------------------------------------------------------------------
@decorator
def etag(target, *args, **kwargs):
    return target(*args,**kwargs)

#-------------------------------------------------------------------------------
# Web - the decorators merged
#-------------------------------------------------------------------------------
# Reference - http://stackoverflow.com/questions/2182858/how-can-i-pack-serveral-decorators-into-one

def chained(*dec_funs):
    def _inner_chain(f):
        for dec in reversed(dec_funs):
            f = dec(f)
        return f
    return _inner_chain

web  = chained(base)
