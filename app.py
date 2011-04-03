from bottle import route, run, static_file, debug, template
import anydbm

import nightlies as magic
debug(True)


@route('/broken/:build')
def broken(build):
    nightlies = get_db()
    if build in nightlies:
        nightlies[build] = "unstable"
        print nightlies

@route('/working/:build')
def working(build):
    nightlies = get_db()
    if build in nightlies:
        nightlies[build] = "working"
        print nightlies

@route('/nightlies')
def nighties():
    return dict(get_db()) #anydbm object not recognized as dict for auto json

@route('/')
@route('/index.html')
def index():
    htmls = ''
    db = get_db()
    for x in db:
        htmls = htmls + ("<div class='%s' id='%s'>%s</div>" %(db[x],x, x))
    
    return template('index.html', htmls=htmls)

@route('/js/:filename')
@route('/css/:filename')
def server_static(filename):
    return static_file(filename, root='./')

def get_db():
    return anydbm.open('nighties', 'c')

run(host='localhost', port=8080, reloader=True)