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


def copy_and_link(origin_path, destination_path):
    """
    :param from_path: current folder location
    :param to_path: destination folder location
    :return: void

    This function leverages the subprocess module to run robocopy to create
    a copy of the app folder in the destination folder.
    Additionally, it creates a directory junction (symlink)
    to keep other potential resources working.
    """
    subprocess.run(
        [
            "robocopy",
            origin_path,
            f"{destination_path}\\{path.basename(origin_path)}",
            "/sec",
            "/move",
            "/e"
        ],

        shell=True,
        check=True
    )
    if path.exists(origin_path):
        subprocess.run(
            [
                "rmdir",
                "/S",
                "/Q",
                origin_path
            ],

            shell=True,
            check=True
        )
    subprocess.run(
        [
            "cmd.exe",
            "/c",
            "mklink",
            "/J",
            origin_path,
            f"{destination_path}\\{path.basename(origin_path)}"
        ],

        shell=True,
        check=True
    )


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
