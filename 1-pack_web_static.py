#!/usr/bin/python3
"""Fabric script for archiving"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Compress the contents of web_static folder into a .tgz archive"""
    try:
        # Create the 'versions' directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Generate the current date and time for the archive name
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Create the archive name
        archive_name = "web_static_" + timestamp + ".tgz"

        # Compress the contents of the web_static folder into a .tgz archive
        local("tar -czvf versions/{} web_static".format(archive_name))

        # Return the archive path if the archive has been correctly generated
        return os.path.join("versions", archive_name)

    except Exception as e:
        # Print an error message if an exception occurs
        print("Error:", e)
        return None

# Example usage:
# result = do_pack()
# if result:
#     print("Archive generated:", result)
# else:
#     print("Failed to generate archive.")
