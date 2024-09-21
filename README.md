# Copy and Link Script

This Python script allows you to copy a directory from one location to another and create a directory junction (symbolic link) for easy access.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Options](#options)
- [Example](#example)
- [Functionality](#functionality)
- [License](#license)

## Features

- **Copy Files**: Utilizes `robocopy` to efficiently copy files and directories.
- **Create Junctions**: Automatically creates a directory junction to maintain accessibility to the copied files.

## Requirements

- **Python 3.x**: Ensure that Python 3 is installed on your system.
- **Windows OS**: The script is designed to work on Windows due to the use of `robocopy` and `mklink`.

## Usage
#### It's recommended to create a [System Restore Point](https://www.windowscentral.com/how-use-system-restore-windows-11#create_restore_point_windows11) before proceeding with any changes.
To run the script, open a Command Prompt or PowerShell, navigate to the directory where the script is located, and execute the following command:

```python copy_to_ssd.py <from_path> <to_path>```

## Options

- --help: Show help information and exit the script.

## Example

To copy a directory from C:\Users\Marcello\Kali to D:\Programs and create a junction, run:

```python  copy_to_ssd.py "C:\Users\Marcello\Kali" "D:\Programs"```

To see usage information, run:

```python copy_to_ssd.py --help```

## Functionality

The script leverages the subprocess module to run robocopy, which handles the copying of the specified directory. After copying, it deletes the original directory and creates a junction at the original location, pointing to the new destination.

### Arguments

- **from_path**: The path of the directory to copy.
- **to_path**: The destination path where the directory will be copied.

## License

Feel free to use this project however you like!

This project is licensed under the MIT License. Check the [LICENSE](https://opensource.org/licenses/MIT) for more details.

