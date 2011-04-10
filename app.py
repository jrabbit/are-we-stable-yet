from bottle import route, run, static_file, debug, template, default_app
from paste import httpserver
import time
import anydbm

import nightlies as magic
debug(True)

@route('/broken/:build/:trac')
@route('/broken/:build')
def broken(build, **kwargs):
    nightlies = get_db()
    if build in nightlies:
        if 'trac' in kwargs:
            nightlies[build] = "unstable %s" % kwargs['trac']
        else:
            nightlies[build] = "unstable"

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
@route('/scroll')
@route('/index.html')
def index():
    htmls = ''
    db = get_db()
    l = db.items()
    # l.reverse()
    for x in sorted(l, reverse=True):
        if x[0] not in ['meta', 'last-edit']:
            if len(x[1].split()) > 1:
                trac = "<a href='%s'>%s </a>" % (x[1].split()[1], x[1].split()[1])
            else:
                trac = "&mdash;"
            status = x[1].split()[0]
            htmls = htmls + ("<div> <div class='scroll-content-item ui-widget-header click-bind %s' \
            id='%s'>%s :</br> %s</div> <div class='hidden trac-url'>%s</div></div>" %(status, x[0], x[0], status, trac))
    style = ".scroll-content {width: %spx;float: left;}" % str(len(l) *120)
    
    # print style
    return template('index.html', kind='scroll', htmls=htmls, style=style, edit=db['last-edit'])

@route('/table')
def table():
    htmls = """<table class='revisions'>
    <tr> <th>Revision</th> <th>Status</th> <th>Trac Id</th> </tr>
    
    """
    # initial table stuff
    db = get_db()
    l = db.items()
    for x in sorted(l, reverse=True):
        if x[0] not in ['meta', 'last-edit']:
            status = x[1].split()[0]
            if len(x[1].split()) > 1:
                trac = "<a href='%s'>%s </a>" % (x[1].split()[1], x[1].split()[1])
            else:
                trac = "&mdash;"
            htmls = htmls + ("<tr id='%s-row'> <td class='table-rev'> %s</td> <td id='%s' class='table-status click-bind %s'>%s</td> <td class='trac-url'>%s</td> </tr>" \
            %( x[0], x[0],x[0], status, status, trac) )        
    style = ''
    htmls = htmls + "</table>"
    return template('index.html', kind='table', htmls=htmls, style=style, edit=db['last-edit'])

@route('/js/:filename')
def js_static(filename):
    return static_file(filename, root='./js')
@route('/css/:filename#.+#')
def css_static(filename):
    return static_file(filename, root='./css')

def get_db():
    return anydbm.open('nighties', 'c')
def db_update():
    d = get_db()
    last = time.mktime(time.strptime(d['last-edit'], "%a %b %d %H:%M:%S %Y %Z"))
    now = time.time()
    if last - now > 7200:
        magic.store()
# while 1:
#     db_update()
#run(host='localhost', port=8080, reloader=True)
# httpserver.serve(default_app(), host='192.168.1.45', port=8080)
