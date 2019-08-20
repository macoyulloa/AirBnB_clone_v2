#!/usr/bin/python3
"  generates a .tgz archive from the contents of the web_static "

import tarfile


def do_pack(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
