import pkg_resources
import json
from bottle import run, route, HTTPResponse, static_file


def create_response(body):
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r


@route("/")
def index():
    return pkg_resources.resource_string(__name__, "index.html")


@route("/css/<file_name>")
def css(file_name):
    return pkg_resources.resource_string(__name__, "css/" + file_name)


@route("/download_csv")
def json_test():
    return static_file("test.csv", root="./", download=True)


if __name__ == "__main__":
    run(host="0.0.0.0", port=8080)

