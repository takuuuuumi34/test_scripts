from bottle import app, HTTPResponse, request, response, route, run, static_file, redirect, error
from beaker.middleware import SessionMiddleware
import bcrypt
import redis
import time


session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)


def set_json_body(body):
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r


@route("/")
@route("/index")
def index():
    s = request.environ.get('beaker.session')
    session_str = s.get("session_str")

    if not session_str:
        redirect("/login")
    print(r.get(session_str))

    return """<p>index page</p>"""


@route("/login")
def login():
    return """
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    """


@route("/login", method="POST")
def do_login():
    username = request.forms.get("username")
    password = request.forms.get("password")

    if check_login(username, password):
        s = request.environ.get('beaker.session')
        s['session_str'] = "test_session"
        s.save()
        r.set("test_session", 1)
        return redirect("/index")
    else:
        return "<p>Failed !</p>"


def check_login(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False


@error(404)
def error404(error):
    return "<p>login failed!</p>"

global r
r = redis.StrictRedis(host='localhost', port=6379, db=0)
run(app=app, host="localhost", port=8000, debug=True, reloader=True)
