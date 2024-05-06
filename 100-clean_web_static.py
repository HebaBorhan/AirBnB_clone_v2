#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives"""
from fabric.api import *
from os.path import isdir
env.hosts = ['23.23.73.165', '54.144.141.225']


def do_clean(number=0):
    """Deleting out-of-date archives"""
    try:
        number = int(number)
        if number < 1:
            number = 1

        # Delete unnecessary archives in the versions folder
        with lcd('versions'):
            local('ls -t | tail -n +{} | xargs rm -f'.format(number + 1))

        # Delete unnecessary archives in /data/web_static/releases folder
        with cd('/data/web_static/releases'):
            files = run('ls -t | tail -n +{} | grep -v "^d"'.format(number + 1)).split()
            # Remove files only, keep directories intact
            [run('rm -rf {}'.format(file)) for file in files]

        return True
    except Exception as e:
        return False
