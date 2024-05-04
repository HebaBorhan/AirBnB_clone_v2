#!/usr/bin/python3
"""Fabric script for archiving."""
from fabric.api import *
from datetime import datetime
import os

def do_pack():
    """Compress the contents of web_static folder into a .tgz archive"""
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
