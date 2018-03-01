from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server


def simple_app(env, start_response):
    setup_testing_defaults(env)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    response_body = [("%s: %s\n" % (key, value)).encode("utf-8") for key, value in env.items()]

    return response_body


httpd = make_server('', 8000, simple_app)
httpd.handle_request()
