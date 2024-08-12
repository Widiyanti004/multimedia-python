import pygame
import PIL
import cv2
import moviepy
import pydub
import tkinter as tk
from pkg_resources import get_distribution, DistributionNotFound

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    print("✅ MoviePy version:", moviepy.__version__)

    # Pydub version (since pydub does not have a __version__ attribute)
    try:
        pydub_version = get_distribution("pydub").version
        print("✅ Pydub version:", pydub_version)
    except DistributionNotFound:
        print("❌ Pydub is not installed")

    # Tkinter check
    try:
        tk_version = tk.TkVersion
        print(f"✅ Tkinter is installed and working! Version: {tk_version}")
    except Exception as e:
        print(f"❌ Error with Tkinter: {e}")

if __name__ == "__main__":
    check_installation()
