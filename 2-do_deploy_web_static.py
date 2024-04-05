#!/usr/bin/python3
"""Module to distribute an archive to servers"""
from fabric.api import *
import shlex
import os


env.hosts = ["54.209.10.115", "54.158.220.44"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """Function to distribute an archive to servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        name_wex = name.replace('.', ' ')
        name_wex = shlex.split(name_wex)
        name_wex = name_wex[0]

        releases_path = "/data/web_static/releases/{}".format(name_wex)
        tmp_path = "/tmp/{}".format(name)

        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(releases_path))
        run('tar -xvzf {} -C {}'.format(tmp_path, releases_path))
        run('rm {}'.format(tmp_path))
        run('mv {}web_static/* {}'.format(releases_path, releases_path))
        run('rm -rf {}web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        return True
    except Exception:
        return False
