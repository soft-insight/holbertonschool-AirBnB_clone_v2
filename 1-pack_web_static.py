#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from os.path import isdir
import fabric.api


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            fabric.api.local("mkdir versions")
        file_name = f"versions/web_static_{date}.tgz"
        fabric.api.local(f"tar -cvzf {file_name} web_static")
        return file_name
    except Exception:
        return None
