"""server."""
import argparse
import numpy as np
from bottle import run, route, request


@route('/post_file', method='POST')
def post_file():
    a = request.params.file_data.split()
    b = [row.split(',') for row in a]
    print(np.array(b))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='post file test.')
    parser.add_argument('--host', default='0.0.0.0', help='Server address')
    parser.add_argument('--port', default=8080, type=int, help='Server port')

    args = parser.parse_args()
    run(host=args.host, port=args.port, debug=False, reloader=False)
