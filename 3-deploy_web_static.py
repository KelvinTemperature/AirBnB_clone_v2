#!/usr/bin/python3
"""Module that creates and distributes an archive to the servers"""
from fabric.api import *
import os


do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ["54.209.10.115", "54.158.220.44"]
env.user = "ubuntu"


def deploy():
    """Function to create and distribute an archive to the web servers"""
    try:
        archive_path = do_pack()
    except Exception:
        return False

    return do_deploy(archive_path)
