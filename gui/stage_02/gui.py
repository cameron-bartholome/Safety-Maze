"""
stage_02/gui.py

This module defines the full GUI layout for Stage 2 of the SafetyMaze project using DearPyGui.
It includes panels for maze selection, input parameters, visual simulation, and laser controls.
The layout is responsive and organized to fit standard desktop resolutions (16:9) 1280x720
"""

import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# ignore red error vs code mis interperating files, can remove later if annoying.

class Stage2MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Safety Maze Stage 2")
        self.setFixedSize(QSize(1280, 720))  # 16:9 ratio
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)

def run_gui():
    app = QApplication(sys.argv)
    window = Stage2MainWindow()
    window.show()
    app.exec()

