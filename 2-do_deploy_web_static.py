#!/usr/bin/python3
"""
A fabric script based on 1-pack_web_static.py file
"""

from datetime import datetime
from fabric.api import local, env, run, put
import os


# Connect to 2 servers
env.hosts = ["34.229.69.59", "54.85.196.44"]
env.user = "ubuntu"

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


def do_deploy(archive_path):
    """
    Distribute the archive to the webservers
    """
    if not os.path.exists(archive_path):
        return False

    put(archive_path, "/tmp/")
    # get the name of the file
    # right now its smthing like /versions/archives.tgz

    filename = archive_path.split("/")[-1]  # only left with archives.tgz

    # remove the extension
    new_path = f"/data/web_static/releases/{filename.split('.')[0]}"

    run(f"sudo mkdir -p {new_path}")

    # extract the compressed archive files
    run(f"sudo tar -xzf /tmp/{filename} -C {new_path}")

    # Delete the archive from the web server
    run(f"sudo rm /tmp/{filename}")

    # Move contents to the current symlink (directory)
    run(f"sudo rsync -a {new_path}/web_static/* {new_path}/")

    # Delete the symbolic link /data/web_static/current
    run("sudo rm -rf /data/web_static/current")

    # Create a new symbolic link /data/web_static/current
    run(f"sudo ln -s {new_path} /data/web_static/current")

    return True
