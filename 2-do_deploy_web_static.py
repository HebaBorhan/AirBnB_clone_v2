#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import *
from os import path


env.hosts = ['23.23.73.165', '54.144.141.225']

def do_deploy(archive_path):
    """Distributing an archive to my web servers"""
    if not path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_folder = '/data/web_static/releases/{}'.format(archive_name[:-4])
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(archive_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, archive_folder))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {}/web_static/* {}'.format(archive_folder, archive_folder))
        run('rm -rf {}/web_static'.format(archive_folder))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(archive_folder))
        return True
    except:
        return False
