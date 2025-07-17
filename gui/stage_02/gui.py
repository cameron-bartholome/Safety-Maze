"""
stage_02/gui.py

This module defines the full GUI layout for Stage 2 of the SafetyMaze project using DearPyGui.
It includes panels for maze selection, input parameters, visual simulation, and laser controls.
The layout is responsive and organized to fit standard desktop resolutions (16:9) 1280x720
"""

import sys
from PyQt6.QtCore import QSize, Qt

from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout,
    QWidget, QHBoxLayout, QFrame, QComboBox, QGroupBox, QLineEdit)

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

        #----------------------------------------------------------------------------------------
        def update_dimension_inputs(self, keys):
            # Clear previous inputs
            for row in self.dimension_rows:
                row.setParent(None)
            self.dimension_rows.clear()

            for key in keys:
                row = QHBoxLayout()

                label = QLabel(key)
                input_box = QLineEdit()
                tolerance_box = QLineEdit()

                input_box.setPlaceholderText("Value")
                tolerance_box.setPlaceholderText("Tolerance")

                label.setStyleSheet("color: black;")
                input_box.setStyleSheet("color: black; background-color: white;")
                tolerance_box.setStyleSheet("color: black; background-color: white;")

                row_container = QFrame()
                row_layout = QHBoxLayout()
                row_layout.addWidget(label)
                row_layout.addWidget(input_box)
                row_layout.addWidget(tolerance_box)
                row_container.setLayout(row_layout)

                self.dimension_frame.layout().addWidget(row_container)
                self.dimension_rows.append(row_container)

        #----------------------------------------------------------------------------------------

        # -------- LEFT PANEL: Maze Selection + Inputs --------
        # DEV-2025-07-17 - Styled Left Panel (text, border, dropdown)

        left_panel = QFrame()
        left_panel.setFrameShape(QFrame.Shape.Box)
        left_panel.setFixedWidth(250)
        left_panel.setStyleSheet("background-color: #dbeeff;border: 1px solid #ccc;")

        left_panel_layout = QVBoxLayout()
        left_panel_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        left_panel_layout.setContentsMargins(5, 20, 5, 10)  # (left, top, right, bottom)


        # Maze Selection GroupBox
        maze_group = QGroupBox()
        maze_group.setStyleSheet("background-color: #dbeeff; border: none;")
        maze_group.setFixedHeight(100)

        maze_group_layout = QVBoxLayout()
        maze_group_layout.setSpacing(5)

        # Maze selection title
        maze_label = QLabel("Maze Selection")
        maze_label.setStyleSheet("font-weight: bold; font-size: 12pt; color: black;")
        maze_label.setFixedHeight(30)


        # Maze dropdown
        maze_selector = QComboBox()
        maze_selector.addItems([
            "Maze 1 - Straight",
            "Maze 2 - L Shape",
            "Maze 3A - Z Shape",
            "Maze 3B - U Shape",
            "Maze 4A - Snake Shape",
            "Maze 4B - Stair Shape"])

        maze_dimensions = {
            "Maze 1 - Straight": ["L1", "G1"],
            "Maze 2 - L": ["L1", "G1", "L2", "G2"],
            "Maze 3A - Z Shape": ["L1", "G1", "L2", "G2", "L3", "G3"],
            "Maze 3B - U Shape": ["L1", "G1", "L2", "G2", "L3", "G3"],
            "Maze 4A - Snake Shape": ["L1", "G1", "L2", "G2", "L3", "G3", "L4", "G4", "L5", "G5"],
            "Maze 4B - Stair Shape": ["L1", "G1", "L2", "G2", "L3", "G3", "L4", "G4", "L5", "G5"]
            }

        def on_maze_selected():
            selection = maze_selector.currentText()
            keys = maze_dimensions.get(selection, [])
            self.update_dimension_inputs(keys)

        def updateDimensionInput(self, maze_name):
        # Placeholder logic, just prints for now
            print(f"Selected maze: {maze_name}")


        maze_selector.currentIndexChanged.connect(on_maze_selected)
        maze_selector.setStyleSheet("font-size: 10pt; color: black; background-color: white;" \
        "padding: 4px;")

        maze_selector.setFixedHeight(30)

        # -------- DIMENSIONS SECTION --------
        dimension_group = QGroupBox("Dimension Inputs (mm)")
        dimension_layout = QVBoxLayout()

        # Store rows here for updating later
        self.dimension_rows = []

        # Create a frame to hold dynamic input fields
        self.dimension_frame = QFrame()
        self.dimension_frame.setLayout(dimension_layout)
        self.dimension_frame.setStyleSheet("background-color: #e6f0ff;")

        # Group layout
        dimension_group_layout = QVBoxLayout()
        dimension_group_layout.addWidget(self.dimension_frame)
        dimension_group.setLayout(dimension_group_layout)

        # Add to left panel layout
        left_panel_layout.addWidget(dimension_group)

        #----------------------------------------------------------------------------------------

        # Add label and dropdown to group
        maze_group_layout.addWidget(maze_label)
        maze_group_layout.addWidget(maze_selector)
        maze_group.setLayout(maze_group_layout)

        left_panel_layout.addWidget(maze_group)
        left_panel.setLayout(left_panel_layout)

        #----------------------------------------------------------------------------------------


        # -------- CENTER PANEL: Maze Drawing Canvas --------
        center_panel = QLabel("Center Viewport")
        center_panel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center_panel.setStyleSheet("background-color: #eeeeee; border: 1px solid #ccc; " \
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
