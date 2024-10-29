
# Keylogger Tool

This tool is a simple keylogger application that records user keystrokes. It is written using the `pynput` library and can be run from the command line.

## Features

- Captures keystrokes and saves them in a file named `key-logger.txt` on the desktop.
- Responds appropriately to special keys like `space`, `tab`, and `backspace`.
- Starts the keylogger with the `--start` argument.

## Requirements

To run this tool, the following library is required:

- **pynput**: You can install this library using the following command:
  ```bash
  pip install pynput
  ```

## Installation

1. Save this code in a Python file, for example, `keylogger.py`.
2. Ensure that Python is installed on your system.

## Usage

To run the tool, enter the following command in the terminal:

```bash
python keylogger.py --start
```

This command starts the keylogger and saves all keyboard inputs in a file named `key-logger.txt` on your desktop.

### Keys

- **Esc**: Stops the keylogger.
- **Space** and **Tab**: Recorded as spaces.
- **Backspace**: Deletes the last character.

## Example Usage

```bash
python keylogger.py --start
```

This command will display the message "Keylogger starting..." in the terminal and run the keylogger in the background, saving all inputs to the `key-logger.txt` file on your desktop.

## Warning

This software is developed for educational purposes only. Please note that the unauthorized use of keyloggers can be illegal. Use it only on your own devices or where you have permission.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details