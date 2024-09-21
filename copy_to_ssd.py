#!/usr/bin/env python3
import subprocess
import sys
from os import path

def print_help():
    help_text = """
Usage: python copy_and_link.py <from_path> <to_path>

Copy a directory from <from_path> to <to_path> and create a directory junction.

Arguments:
  from_path   The path of the directory to copy.
  to_path     The destination path where the directory will be copied.
  
Options:
  --help      Show this help message and exit.

"""
    print(help_text)

def copy_and_link(from_path, to_path):
    """
    :param from_path: current folder location
    :param to_path: destination folder location
    :return: void

    This function leverages the subprocess module to run robocopy to create a copy of the app folder in the destination folder.
    Additionally, it creates a directory junction (symlink) to keep other potential resources working.
    """
    subprocess.run(["robocopy", from_path, f"{to_path}\\{path.basename(from_path)}", "/sec", "/move", "/e"], shell=True)
    if path.exists(from_path):
        subprocess.run(["rmdir", "/S", "/Q", from_path], shell=True)
    subprocess.run(["cmd.exe", "/c", "mklink", "/J", from_path, f"{to_path}\\{path.basename(from_path)}"], shell=True)


# Example usage
if __name__ == "__main__":
    try:
        if sys.argv[1] == "--help":
            print_help()
            sys.exit(0)
        from_path, to_path = sys.argv[1:3]
        copy_and_link(from_path, to_path)
        sys.exit(0)
    except Exception as e:
        print(e)
        print_help()
        sys.exit(0)


