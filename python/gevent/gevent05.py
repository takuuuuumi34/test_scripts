import json
import random

from gevent import pywsgi, sleep
from geventwebsocket.handler import WebSocketHandler


class WebSocketApp(object):
    def __call__(self, environ, start_response):
        ws = environ['wsgi.websocket']
        x = 0
        while True:
            data = json.dump({'x': x, 'y': random.randint(1,5)})
            ws.send(data)
            x += 1
            sleep(1)


server = pywsgi.WSGIServer(('', 10000), WebSocketApp(), handler_class=WebSocketHandler)
server.serve_forever()
