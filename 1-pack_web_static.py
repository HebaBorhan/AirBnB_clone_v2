#!/usr/bin/python3
"""Fabric script for archiving."""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Compress the contents of web_static folder into a .tgz archive"""
    current = datetime.now()
    compress = 'web_static_' + current.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(
        compress), capture=True)
    if result.succeeded:
        return compress
    else:
        return None
