"""
stage_02/gui.py

This module defines the full GUI layout for Stage 2 of the SafetyMaze project using DearPyGui.
It includes panels for maze selection, input parameters, visual simulation, and laser controls.
The layout is responsive and organized to fit standard desktop resolutions (16:9) 1280x720
"""

import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QLabel
# ignore red error vs code mis-interperating files, can remove later if annoying.

class Stage2MainWindow(QMainWindow):
    """
    Main window class for Stage 2 of the Safety Maze application.

    This window includes:
    - Top navigation bar to indicate progress through simulation steps.
    - Left panel for maze selection and input configuration.
    - Center canvas for maze drawing and laser visualization.
    - Right panel for laser beam control inputs and results display.
    """

    def __init__(self):
        super().__init__()
        # -------- Window Setup --------
        self.setWindowTitle("Safety Maze Stage 2")
        self.setFixedSize(QSize(1280, 720))  # 16:9 ratio
        self.setStyleSheet("background-color: #f8fafc;")  # Tailwind's light gray (near white)


        # -------- TOP: Progress Bar Section --------
        # DEV-2025-07-14-01 Stage 2 - GUI Layout implementation
        top_bar = QWidget()
        top_bar.setFixedHeight(50)
        top_layout = QHBoxLayout()

        steps = [
            "1 Select Maze",
            "2 Adjust Dimensions",
            "3 Choose Material",
            "4 Configure Beam",
            "5 View Results"
        ]

        for i, step in enumerate(steps):
            step_label = QLabel(step)
            step_label.setStyleSheet("color: #1e293b; font-weight: bold; padding: 4px;")
            top_layout.addWidget(step_label)

            if i < len(steps) - 1:
                arrow = QLabel("→")
                arrow.setStyleSheet("color: #94a3b8; padding: 4px;")
                top_layout.addWidget(arrow)

        top_bar.setLayout(top_layout)  # sets layout as we specified above
        self.setMenuWidget(top_bar) # adds widget to main window menu bar



        # -------- LEFT PANEL: Maze Selection + Inputs --------
        left_panel = QLabel("Left Panel")
        left_panel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_panel.setFixedWidth(250)
        left_panel.setStyleSheet("color: black; font-weight: bold;")

        left_panel.setStyleSheet("background-color: #d9eaf7; border: 1px solid #aaa;" \
        "color: black; font-weight: bold;")




        # --------CENTER PANEL: Maze Viewer / Canvas --------
        center_panel = QLabel("Center Viewport")
        center_panel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        center_panel.setStyleSheet("background-color: #eeeeee; border: 1px solid #aaa;" \
        "color: black; font-weight: bold;")




        # -------- RIGHT PANEL: Laser Controls + Results --------
        right_panel = QLabel("Laser Controls")
        right_panel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_panel.setFixedWidth(250)

        right_panel.setStyleSheet("background-color: #fbe6d4; border: 1px solid #aaa;" \
        "color: black; font-weight: bold;")



        # -------- COMBINE PANELS INTO MAIN LAYOUT --------
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        central_layout.addWidget(top_bar)

        body_layout = QHBoxLayout()
        body_layout.addWidget(left_panel)
        body_layout.addWidget(center_panel, stretch=1)
        body_layout.addWidget(right_panel)

        central_layout.addLayout(body_layout)



#------------------------------------------------------------------------------------------

def run_gui():
    """
    Launches the Stage 2 GUI window for the Safety Maze application.
    Initializes the main window, canvas, and controls for the laser beam simulation.
    """
    app = QApplication(sys.argv)
    window = Stage2MainWindow()
    window.show()
    app.exec()
