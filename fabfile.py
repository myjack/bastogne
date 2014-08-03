from fabric.api import cd, run, env, sudo


env.user = 'maguowei'
env.hosts = ['bastogne.chinacloudapp.cn']


def init():
    with cd('~/www'):
        run('git clone https://github.com/maguowei/bastogne.git')
        with cd('bastogne'):
            run('mongoimport -d bastogne -c movie --file data/movie.json')
            run('mongoimport -d bastogne -c genres --file data/genres.json')
            with cd('command'):
                run('python3 local_image.py')
                run('python3 complate_search.py')


def deploy():
    with cd('~/www/bastogne'):
        run('git pull')
        sudo('supervisorctl stop all')
        sudo('supervisorctl start all')


if __name__ == '__main__':
    deploy()
