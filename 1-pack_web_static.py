#!/usr/bin/python3
"""Generates archive"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    date_string = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date_string)

    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(file_name))

    if result.failed:
        return None
    else:
        return file_name
