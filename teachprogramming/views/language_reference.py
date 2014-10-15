from pyramid.view import view_config
from pyramid.renderers import render_to_response

from . import web

from teachprogramming.lib.language_reference import generate_languages
from teachprogramming.static.language_reference._test import test_langauges

DEFAULT_PATH = 'teachprogramming/static/language_reference'

@view_config(route_name='language_reference')
@web
def langauage_reference(request):
    return render_to_response(
        'teachprogramming:templates/html/reference/language_reference.mako',
        {
            'language_reference': generate_languages(default_path=DEFAULT_PATH),
            'language_tests': test_langauges(default_path=DEFAULT_PATH),
        },
        request=request,
    )
