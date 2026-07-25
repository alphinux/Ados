import os
import subprocess

def open_instagram():
    # Your specific Instagram profile link
    url = "https://www.instagram.com/alphinux7?igsh=MWlqODFlbDJkNmQ0cg=="
    
    print("FOLLOW ON INSTAGRAM...")
    
    try:
        # termux-open triggers Android to open the link in the default app or browser
        subprocess.run(["termux-open", url], check=True)
    except FileNotFoundError:
        print("Error: termux-api is not installed or configured correctly.")

if __name__ == "__main__":
    open_instagram()

