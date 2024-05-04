#!/usr/bin/python3
"""Fabric script for archiving."""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Compress the contents of web_static folder into a .tgz archive"""
    current = datetime.now()
    compress = 'web_static_' + current.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(compress))
    if create is not None:
        return compress
    else:
        return None
