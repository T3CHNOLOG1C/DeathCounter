import keyboard
import os
import time

FILE_NAME = "deathcount.txt"

def get_count():
    """Read the current death count from the file.
    Uses a retry loop if an error occurs, and always closes the file immediately."""
    retries = 5
    while retries:
        try:
            if not os.path.exists(FILE_NAME):
                # Create file with initial count 0 if it doesn't exist.
                with open(FILE_NAME, "w") as f:
                    f.write("0")
                return 0
            with open(FILE_NAME, "r") as f:
                content = f.read().strip()
                return int(content) if content else 0
        except Exception as e:
            print(f"Error reading file: {e}. Retrying...")
            retries -= 1
            time.sleep(0.1)
    return 0

def update_count(new_count):
    """Write the new count to the file.
    Uses a retry loop and ensures the file is only open briefly."""
    retries = 5
    while retries:
        try:
            with open(FILE_NAME, "w") as f:
                f.write(str(new_count))
            print(f"Death count updated to: {new_count}")
            return
        except Exception as e:
            print(f"Error writing file: {e}. Retrying...")
            retries -= 1
            time.sleep(0.1)
    print("Failed to update the file after multiple attempts.")

def increase():
    """Increase the death count by one."""
    count = get_count()
    update_count(count + 1)

def decrease():
    """Decrease the death count by one."""
    count = get_count()
    update_count(count - 1)

# Register hotkeys with keys recognized by the keyboard module.
keyboard.add_hotkey("ctrl+shift+num plus", increase)
keyboard.add_hotkey("ctrl+shift+num minus", decrease)

print("Script running. Press ctrl+shift+= to increase and ctrl+shift+- to decrease the death count.")
keyboard.wait()