import logging
import datetime

import falcon

log = logging.getLogger(__name__)

ITEMS = {
    1: {  # have test data in system on startup
        'id': 1,
        'user_id': "user1234",
        'keywords': ["hammer", "nails", "tools"],
        "description": "A hammer and nails set",
        "lat": 51.2798438, 
        "lon": 1.0830275,
        "date_from": datetime.datetime.now().isoformat(),
    }
}

class AddCORSMiddleware:
    def process_request(self, req, resp):
        resp.set_headers({
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS, DELETE",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
        })

class IndexResource:
    def on_options(self, req, resp):
        resp.status = falcon.HTTP_204
    def on_get(self, req, resp):
        resp.content_type = falcon.MEDIA_HTML
        resp.text = """<html><head><title>Test</title></head><body><h1>Test</h1></body></html>"""

class ItemsResource:
    def on_options(self, req, resp):
        resp.status = falcon.HTTP_204
    def on_get(self, req, resp):
        items = tuple(ITEMS.values())
        if req.params.get('user_id'):
            items = tuple(i for i in items if i['user_id'] == req.params.get('user_id'))
        resp.media = items

class ItemResource:
    def on_options(self, req, resp):
        resp.status = falcon.HTTP_204
    def on_head(self, req, resp):
        pass  # TODO: cant remember why this is a null implementation - maybe it can be removed?
    def on_post(self, req, resp):
        item_id = max(ITEMS.keys()) + 1
        FIELDS = frozenset(req.media.keys())
        REQUIRED_FIELDS = frozenset(('user_id','keywords',"description","lat","lon",))
        if not REQUIRED_FIELDS.issubset(FIELDS):
            resp.status = falcon.HTTP_405
            return
        ITEMS[item_id] = req.media
        ITEMS[item_id].update({
            "id": item_id,
            "date_from": datetime.datetime.now().isoformat(),
        })
        resp.status = falcon.HTTP_201
        resp.media = ITEMS[item_id]
    def on_get(self, req, resp, item_id):
        try:
            resp.media = ITEMS[int(item_id)]
        except KeyError:
            resp.status = falcon.HTTP_404
    def on_delete(self, req, resp, item_id):
        try:
            del ITEMS[int(item_id)]  # TODO: this is terrible because it re-uses ids .. 
            resp.status = falcon.HTTP_204
        except KeyError:
            resp.status = falcon.HTTP_404


def create_wsgi_app(**kwargs):
    app = falcon.App(middleware=[
        AddCORSMiddleware(),
    ])
    app.add_route('/', IndexResource())
    app.add_route('/item', ItemResource())
    app.add_route('/item/{item_id}', ItemResource())
    app.add_route('/items', ItemsResource())
    return app

app = create_wsgi_app()  # surface `app` variable for gunicorn and other wsgi servers

if __name__ == '__main__':
    kwargs = {"host": "0.0.0.0", "port": 8000, "log_level": logging.DEBUG}  # TODO: get kwargs from argparse
    logging.basicConfig(level=kwargs['log_level'])

    from wsgiref import simple_server
    httpd = simple_server.make_server(kwargs['host'], kwargs['port'], create_wsgi_app(**kwargs))
    try:
        log.info('start')
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
