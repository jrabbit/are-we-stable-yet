from bottle import route, run, static_file, debug, template
import anydbm

import nightlies as magic
debug(True)


@route('/broken/:build')
def broken(build):
    nightlies = get_db()
    if build in nightlies:
        nightlies[build] = "unstable"
        # print nightlies

@route('/working/:build')
def working(build):
    nightlies = get_db()
    if build in nightlies:
        nightlies[build] = "working"
        # print nightlies

@route('/nightlies')
def nighties():
    return dict(get_db()) #anydbm object not recognized as dict for auto json

@route('/')
@route('/index.html')
def index():
    htmls = ''
    db = get_db()
    l = db.items()
    l.reverse()
    for x in l:
        if x[0] not in ['meta', 'last-edit']:
            htmls = htmls + ("<div class='scroll-content-item ui-widget-header' \
            id='%s'>%s :</br> %s</div>" %(x[0], x[0], x[1]))
    style = ".scroll-content {width: %spx;float: left;}" % str(len(l) *120)
    # print style
    return template('index.html', htmls=htmls, style=style)

@route('/js/:filename')
def js_static(filename):
    return static_file(filename, root='./js')
@route('/css/:filename#.+#')
def css_static(filename):
    return static_file(filename, root='./css')

def get_db():
    return anydbm.open('nighties', 'c')

run(host='localhost', port=8080, reloader=True)