from pyramid.config import Configurator
from pyramid_beaker import set_cache_regions_from_settings
import pyramid.events


from .templates import helpers as template_helpers


#from sqlalchemy import engine_from_config
#from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    set_cache_regions_from_settings(settings)
    
    # SQLA not used in this project
    #engine = engine_from_config(settings, 'sqlalchemy.')
    #DBSession.configure(bind=engine)
    
    config = Configurator(settings=settings)
    
    config.add_static_view('static'              , 'static'                     ) #cache_max_age=3600
    config.add_static_view('projects/game/images', 'static/projects/game/images')
    
    # Plain Template routes  
    from .templates.helpers import get_templates
    import teachprogramming.views.static_views as static_views
    config.add_route('root', '/')
    config.add_view(static_views.home, route_name='root')
    for route_name in get_templates('static'):
        #print ("register {0}".format(route_name))
        config.add_route(route_name, '/{0}'.format(route_name))
        config.add_view(getattr(static_views,route_name), route_name=route_name)

    
    config.add_route('project'     , '/projects/{project_type}/{project}.{selected_lang}')
    config.add_route('project_code', '/projects/{project_type}/{project}.{selected_lang}/{version}')
    
    # Old for reference
    #config.add_view('myproject.views.mako_test', route_name='mako_test')
    #config.add_route('hello_world', '/hello_world')
    #config.add_route('mako_test', '/mako_test/{one}/{two}') #'/prefix/{one}/{two}'

    # Events -------------------------------------------------------------------
    config.add_subscriber(add_template_helpers_to_event, pyramid.events.BeforeRender)

    # Return -------------------------------------------------------------------
    config.scan()
    return config.make_wsgi_app()

def add_template_helpers_to_event(event):
    event['h'] = template_helpers
    event['selected_lang'] = 'py'
