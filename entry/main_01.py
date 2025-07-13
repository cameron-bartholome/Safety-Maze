"""
Safety Maze – Stage 1
Main entry point for the Safety Maze simulation app.

Launches the Stage 1 GUI for laser beam reflection simulation in a 2D labyrinth.

Author: CB
Date: 2025-06-21
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gui.stage_01 import gui



# --- Launch the GUI ---

print("Launching SafetyMaze...") #test to see it launchers

if __name__ == "__main__":
    gui.run_gui()  # Launch the Stage 1 GUI
