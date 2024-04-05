#!/usr/bin/python3
"""Fabric script to generate archive file"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Function to compress files"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")

        dt = datetime.now()
        f = "%Y%m%d%H%M%S"
        arch_path = 'versions/web_static_{}.tgz'.format(dt.strftime(f))
        local("tar -cvzf {} web_static".format(arch_path))

        return arch_path
    except Exception:
        return None
