import subprocess
import sys

def install_dependencies():
    print("FoleyCrafter: Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "decord", "moviepy"])
        print("FoleyCrafter: Dependencies installed successfully.")
    except Exception as e:
        print(f"FoleyCrafter: Failed to install dependencies: {e}")

if __name__ == "__main__":
    install_dependencies()
