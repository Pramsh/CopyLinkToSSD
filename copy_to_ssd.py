#!/usr/bin/env python3
r"""
copy_and_link.py

This module provides functionality to copy a directory from one location to another
and create a directory junction (symbolic link) for easy access.

Features:
- Uses 'robocopy' to efficiently copy files and directories, maintaining security attributes.
- Creates a junction link at the original directory location, allowing access to the new location.

Usage:
To use this module, run the script with the following command:
python copy_and_link.py <from_path> <to_path>

Parameters:
- from_path (str): The path of the directory to be copied.
- to_path (str): The destination path where the directory will be copied.

Options:
- --help: Displays usage information and exits the script.

Example:
To copy a directory from C:\Users\marcello\Kali to D:\Programs and create a junction,
execute: python copy_and_link.py "C:\Users\marcello\Kali" "D:\Programs"

This script is designed to work on Windows systems and requires Python 3.x.
"""

import subprocess
import sys
from os import path


def print_help():
    """
    prints script instruction
    """
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
    if not path.exists(origin_path) or not path.exists(destination_path):
        print("Insert a valid path")
        print_help()
        sys.exit(0)
    subprocess.run(
        [
            "robocopy",
            origin_path,
            f"{destination_path}\\{path.basename(origin_path)}",
            "/sec",
            "/move",
            "/e",
        ],
        shell=True,
        check=False,
    )
    if path.exists(origin_path):
        subprocess.run(
            [
                "rmdir",
                "/S",
                "/Q",
                origin_path,
            ],
            shell=True,
            check=False,
        )
    subprocess.run(
        [
            "cmd.exe",
            "/c",
            "mklink",
            "/J",
            origin_path,
            f"{destination_path}\\{path.basename(origin_path)}",
        ],
        shell=True,
        check=False,
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
    except ValueError as e:
        print(e)
        print_help()
        sys.exit(0)