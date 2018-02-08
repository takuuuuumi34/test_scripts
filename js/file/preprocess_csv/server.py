"""server."""
import argparse
import pandas as pd
from bottle import run, route, request, static_file, HTTPResponse


def set_json_body(body):
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r


@route('/', method='GET')
def index():
    return static_file("index.html", root='.')


@route('/post_file', method='POST')
def post_file():
    binary_data = request.params.file_data.split()
    file_data = [row.split(',') for row in binary_data]
    df = pd.DataFrame(file_data).astype('float')
    print(df.describe())
    r = set_json_body({"test": "hoge"})
    return r


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='post file test.')
    parser.add_argument('--host', default='0.0.0.0', help='Server address')
    parser.add_argument('--port', default=8080, type=int, help='Server port')

    args = parser.parse_args()
    run(host=args.host, port=args.port, debug=False, reloader=False)
