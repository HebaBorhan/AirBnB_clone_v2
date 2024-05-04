#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers"""
from fabric.api import *
from os import path
from datetime import datetime
env.hosts = ['23.23.73.165', '54.144.141.225']


def do_pack():
    """Compress the contents of web_static folder into a .tgz archive"""
    try:
        if not isdir("versions"):
            local("mkdir -p versions")
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(date_time)
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        print("Error occurred during archive creation:", str(e))
        return None


def do_deploy(archive_path):
    """Distribute an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        remote_path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(remote_path, folder_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(
            file_name, remote_path, folder_name))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(remote_path, folder_name))
        run('rm -rf {}{}/web_static'.format(remote_path, folder_name))
        run('rm -rf /data/web_static/current')

        # Create new symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(
            remote_path, folder_name))

        return True

    except Exception as e:
        return False


def deploy():
    """Create and distribute an archive to the web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
