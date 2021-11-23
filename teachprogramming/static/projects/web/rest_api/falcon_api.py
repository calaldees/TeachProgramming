import logging
import random
import datetime

import falcon

log = logging.getLogger(__name__)

ITEMS = {
    1: {
        'id': 1,
        'user_id': "user1234",
        'keywords': ["hammer", "nails", "tools"],
        "description": "A hammer and nails set",
        "lat": (random.random() * (70*2)) - 70,
        "lon": (random.random() * (180*2)) - 180,
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
        resp.text = """
<html>
<head>
<title>Test</title>
</head>
<body>
<h1>Test</h1>
</body>
</html>
"""

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
        pass

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
        item_id = int(item_id)
        try:
            resp.media = ITEMS[item_id]
        except KeyError:
            resp.status = falcon.HTTP_404

    def on_delete(self, req, resp, item_id):
        item_id = int(item_id)
        try:
            del ITEMS[item_id]  # TODO: this is terrible because it re-uses ids .. 
            resp.status = falcon.HTTP_201
        except KeyError:
            resp.status = falcon.HTTP_404

app = falcon.App(middleware=[
    AddCORSMiddleware(),
])


index_resource = IndexResource()
app.add_route('/', index_resource)

item_resource = ItemResource()
app.add_route('/item', item_resource)
app.add_route('/item/{item_id}', item_resource)

items_resource = ItemsResource()
app.add_route('/items', items_resource)


if __name__ == '__main__':
    #kwargs = get_args()
    kwargs = {
        "host": "0.0.0.0",
        "port": 8000
    }
    logging.basicConfig(level=logging.DEBUG)  #kwargs['log_level']

    from wsgiref import simple_server
    httpd = simple_server.make_server(kwargs['host'], kwargs['port'], app)  #create_wsgi_app(**kwargs)
    try:
        log.info('start')
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
