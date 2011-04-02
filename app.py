from bottle import route, run, static_file
import anydbm

@route('/hello')
def hello():
    return "Hello World!"

@route('/broken/:build')
def broken(build):
    # nightlies = {u'r41096': "unkown"}
    nightlies = get_db()
    nightlies[build] = "unstable"
    print nightlies

@route('/nightlies')
def nighties():
    return dict(get_db()) #anydbm object not recognized as dict for auto json

@route('/js/:filename')
@route('/css/:filename')
def server_static(filename):
    return static_file(filename, root='./static')

def get_db():
    return anydbm.open('nighties', 'c')

run(host='localhost', port=8080)