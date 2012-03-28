from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    config.add_route('home', '/')
    config.add_route('project_doc' , '/project/{project}.{format}')
    #config.add_route('project_code', '/code/{project}.{format}'          )
    config.add_route('project_code', '/code/{project}.{format}/{version}')
    
    # Old for reference
    #config.add_view('myproject.views.mako_test', route_name='mako_test')
    #config.add_route('hello_world', '/hello_world')
    #config.add_route('mako_test', '/mako_test/{one}/{two}') #'/prefix/{one}/{two}'

    config.scan()
    return config.make_wsgi_app()

