from fabric.api import run, env, cd

env.hosts = ['jrabbit@serenity.jrfxmedia.com']

def update_gunicorn():
    with cd('/home/jrabbit/are-we-stable-yet/'):
        run('pwd')
        run("kill -HUP  `cat gunicorn.pid`")

def start_gunicorn(host='serenity.jrfxmedia.com'):
    with cd('~/are-we-stable-yet'):
        run("gunicorn -b %s:8080 -D -p gunicorn.pid wsgi:application" % host)

def pull():
    with cd('~/are-we-stable-yet'):
        run('eval `ssh-agent` && ssh-add ~/.ssh/id_proj && git pull; kill -9 $SSH_AGENT_PID')
        update_gunicorn()


def initial_deploy():
    run("git clone git://github.com/jrabbit/are-we-stable-yet.git")