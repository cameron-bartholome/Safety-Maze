"""
main_02.py

Entry point for launching Stage 2 GUI using PyQt6.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gui.stage_02 import gui

if __name__ == "__main__":
    print("Launching Safety Maze Stage 2...")
    run_gui()
