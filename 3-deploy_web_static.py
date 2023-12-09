#!/usr/bin/python3
"""Creates and distributes an archive to web servers."""

from fabric.api import env, put, run, local
from os.path import exists, isdir
from datetime import datetime

env.hosts = ['xx-web-01', 'xx-web-02']

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    date_string = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date_string)

    if not isdir("versions"):
        local("mkdir versions")
    result = local("tar -cvzf {} web_static".format(file_name))

    if result.failed:
        return None
    else:
        return file_name

def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not exists(archive_path):
        return False

    try:
        archive_file = archive_path.split("/")[-1]
        archive_root = archive_file.split(".")[0]

        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(archive_root))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_file, archive_root))
        run("rm /tmp/{}".format(archive_file))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive_root, archive_root))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_root))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_root))
        print("New version deployed!")
        return True
    except:
        return False

def deploy():
    """Creates and distributes an archive to web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
