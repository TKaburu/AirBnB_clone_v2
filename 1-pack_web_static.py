#!/usr/bin/python3

"""
A Fabric script that generates a .tgz archive
"""

from datetime import datetime
from fabric.api import local
import os


# Archive folder name versions
# File name format -> web_static_<year><month><day><hour><minute><second>.tgz

def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.
    """

    date = datetime.now().strftime("%Y%m%d%H%M%S")

    # create versions if doesn't exist
    if not os.path.exists("versions"):
        local("mkdir -p versions")
    # path
    path_to_archive = f"versions/web_static_{date}.tgz"

    # archive the files tar [-options] <name of the tar archive> [directory]
    archives = local(f"tar -czvf {path_to_archive} web_static")

    return archives
