#!/usr/bin/python3
"""Fabric script for archiving."""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Compress the contents of web_static folder into a .tgz archive"""
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    c.run('mkdir -p versions')
    create = c.local('tar -cvzf versions/{} web_static'.format(archive))
    if create.failed:
        return None
    else:
        return archive
