# DeathCounter

**DeathCounter** is a lightweight Python app that tracks and updates a numerical death count stored in a text file (`deathcount.txt`) for usage with livestreams. The application listens for global hotkeys to increment (`ctrl+shift+numpad plus`) or decrement (`ctrl+shift+numpad minus`) the death count.

## Features

- **Hotkey Control:** Increase or decrease the death count using global hotkeys.
- **Safe File Handling:** Minimizes file lock duration and employs a retry mechanism.
- **Cross-Platform Executable:** Built with PyInstaller to bundle the script, Python runtime, and required modules into a standalone executable for Windows, Linux, and MacOS.

## Requirements

- Python 3.6 or higher
- [keyboard](https://pypi.org/project/keyboard/) module (`pip install keyboard`)
- [PyInstaller](https://pypi.org/project/pyinstaller/) (`pip install pyinstaller`)

## Usage

### Running the Script

Simply run the Python script (or the python-bundled executable) to start the application:

```bash
python3 deathcounter.py
```

```bash
./deathcounter(.exe)
```

### Building the Executable
A build script (build.py) is provided to bundle the application into a standalone executable. To build:

```bash
python build.py
```

This script uses PyInstaller to create an executable that includes:

- The Python runtime
- All necessary modules

The resulting executable will be located in the ``dist`` folder.

### Customization
Hotkeys:
- Modify the keys on lines 54 and 55 of ``deathcounter.py`` to the keys you want and repackage the script.

### License
This project is open source and available under the Mozilla Public License 2.0.