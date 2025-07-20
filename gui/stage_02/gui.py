"""
stage_02/gui.py

This module defines the full GUI layout for Stage 2 of the SafetyMaze project using DearPyGui.
It includes panels for maze selection, input parameters, visual simulation, and laser controls.
The layout is responsive and organized to fit standard desktop resolutions (16:9) 1280x720
"""

import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QComboBox,
    QFrame, QHBoxLayout, QLineEdit
)

# ========== Stage 2 Main Window ==========
class Stage2MainWindow(QMainWindow):
    """
    Main window for Safety Maze Stage 2.
    Initializes UI components: top progress bar, left input panel,
    central canvas placeholder, and right control panel.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Safety Maze - Stage 2")
        self.setMinimumSize(QSize(1280, 720))

        # ========== Main Layout Wrapper ==========
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # ========== Top Progress Bar ==========
        top_bar = QFrame()
        top_bar.setFrameShape(QFrame.Shape.Panel)
        top_bar.setStyleSheet("background-color: #DDDDDD; color: black; font-weight: bold;")

        top_layout = QHBoxLayout()
        top_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        top_layout.setSpacing(60)

        top_bar.setLayout(top_layout)
        top_layout.addWidget(QLabel("1. Select Maze"))
        top_layout.addWidget(QLabel("→"))
        top_layout.addWidget(QLabel("2. Adjust Geometry"))
        top_layout.addWidget(QLabel("→"))
        top_layout.addWidget(QLabel("3. Choose Materials"))
        top_layout.addWidget(QLabel("→"))
        top_layout.addWidget(QLabel("4. Configure Beam"))
        top_layout.addWidget(QLabel("→"))
        top_layout.addWidget(QLabel("5. View Results"))
        main_layout.addWidget(top_bar)

        # ========== Horizontal Body Layout ==========
        body_frame = QFrame()
        body_layout = QHBoxLayout()
        body_frame.setLayout(body_layout)
        main_layout.addWidget(body_frame)

        # ========== Left Panel: Maze Configuration ==========
        left_panel = QFrame()
        left_panel.setFrameShape(QFrame.Shape.Panel)
        left_panel.setStyleSheet("background-color: #F5F5F5; border: 1px solid gray;")
        left_panel.setFixedWidth(300)
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)

        # Maze Selection Section
        maze_group = QFrame()
        maze_group.setFrameShape(QFrame.Shape.Panel)
        maze_group.setStyleSheet("background-color: #FFFFFF; border: 1px solid #AAA;")
        maze_layout = QVBoxLayout()
        maze_group.setLayout(maze_layout)

        maze_label = QLabel("Maze Selection")
        maze_label.setStyleSheet("color: black; font-weight: bold")
        self.maze_selector = QComboBox()
        self.maze_selector.setStyleSheet("color: black")
        self.maze_selector.addItems([
            "Select a Maze . . .",
            "Maze 1 - Straight",
            "Maze 2 - L",
            "Maze 3A - Z",
            "Maze 3B - U",
            "Maze 4A - Snake",
            "Maze 4B - Stair"
        ])
        self.maze_selector.currentTextChanged.connect(self.on_maze_selected)

        maze_layout.addWidget(maze_label)
        maze_layout.addWidget(self.maze_selector)

        # Dimension Input Section
        dimension_group = QFrame()
        dimension_group.setFrameShape(QFrame.Shape.Panel)
        dimension_group.setStyleSheet("background-color: #FFFFFF; border: 1px solid #AAA")
        self.dimension_inputs_layout = QVBoxLayout()
        dimension_group.setLayout(self.dimension_inputs_layout)

        # Add to left panel
        left_layout.addWidget(maze_group)
        left_layout.addWidget(dimension_group)
        left_layout.addStretch()

        # ========== Central Panel ==========
        central_panel = QFrame()
        central_panel.setStyleSheet("background-color: #FFFFFF; color: black; " \
        "border: 1px solid gray;")
        central_layout = QVBoxLayout()
        central_panel.setLayout(central_layout)
        label = QLabel("[ Maze Viewport Placeholder ]")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        central_layout.addWidget(label)

        # ========== Right Panel ==========
        right_panel = QFrame()
        right_panel.setFrameShape(QFrame.Shape.Panel)
        right_panel.setStyleSheet("background-color: #F5F5F5; color: black; " \
        "border: 1px solid gray;")
        right_panel.setFixedWidth(300)
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)
        label = QLabel("[ Laser Controls Section ]")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(label)
        right_layout.addStretch()

        # Add panels to body layout
        body_layout.addWidget(left_panel)
        body_layout.addWidget(central_panel)
        body_layout.addWidget(right_panel)

    # ========== Maze Selection Handler ==========
    def on_maze_selected(self, text):
        """
        Triggered when a maze is selected from the drop-down.
        Retrieves the required dimension keys based on selection
        and updates the dynamic input fields accordingly.
        """

        maze_dimensions = {
            "Maze 1 - Straight": ["L1", "G1"],
            "Maze 2 - L": ["L1", "G1", "L2", "G2"],
            "Maze 3A - Z": ["L1", "G1", "L2", "G2", "L3", "G3"],
            "Maze 3B - U": ["L1", "G1", "L2", "G2", "L3", "G3"],
            "Maze 4A - Snake": ["L1", "G1", "L2", "G2", "L3", "G3", "L4", "G4", "L5", "G5"],
            "Maze 4B - Stair": ["L1", "G1", "L2", "G2", "L3", "G3", "L4", "G4", "L5", "G5"]
        }
        keys = maze_dimensions.get(text, [])
        self.update_dimension_inputs(keys)

    # ========== Dynamic Dimension Input Updater ==========
    def update_dimension_inputs(self, keys):
        """
        Clears and rebuilds the dimension input fields
        based on the selected maze's requirements.
        Each row includes a label, value input, and tolerance input.
        """

        for i in reversed(range(self.dimension_inputs_layout.count())):
            item = self.dimension_inputs_layout.itemAt(i)
            if item.layout():
                # Clear layout recursively
                while item.layout().count():
                    sub_item = item.layout().takeAt(0)
                    if sub_item.widget():
                        sub_item.widget().deleteLater()
                self.dimension_inputs_layout.removeItem(item)
            elif item.widget():
                item.widget().deleteLater()

        for key in keys:
            row = QHBoxLayout()
            label = QLabel(f"{key}:")
            value_input = QLineEdit()
            value_input.setPlaceholderText("10mm")
            tolerance_input = QLineEdit()
            tolerance_input.setPlaceholderText("±0.5mm")

            # Styling
            label.setStyleSheet("color: black;")  # Label color
            value_input.setStyleSheet("""QLineEdit {color: black; qproperty-alignment: AlignCenter;}
                                      QLineEdit::placeholder {color: gray;}""")
            tolerance_input.setStyleSheet("""QLineEdit {color: black; qproperty-alignment: AlignCenter;}
                                      QLineEdit::placeholder {color: gray;}""")
            label.setFixedWidth(40)
            value_input.setFixedWidth(100)
            tolerance_input.setFixedWidth(100)

            # Format and validate after focus
            value_input.editingFinished.connect(
                lambda v=value_input: v.setText(self.format_mm(v.text())))

            tolerance_input.editingFinished.connect(
                lambda t=tolerance_input: t.setText(self.format_pm(t.text())))


            row.addWidget(label)
            row.addWidget(value_input)
            row.addWidget(tolerance_input)
            self.dimension_inputs_layout.addLayout(row)

    # ========== Helper: Format Values with Units ==========
    def format_mm(self, value: str) -> str:
        """Appends 'mm' to the numeric value, if valid."""
        try:
            float_val = float(value)
            return f"{float_val:.1f} mm"
        except ValueError:
            return value

    def format_pm(self, value: str) -> str:
        """Appends '±' and 'mm' to the numeric value, if valid."""
        try:
            float_val = float(value)
            return f"±{float_val:.1f} mm"
        except ValueError:
            return value



# ========== Launch GUI ==========

def run_gui():
    """
    Launches the Stage 2 GUI window for the Safety Maze application.
    Initializes the main window, canvas, and controls for the laser beam simulation.
    """
    app = QApplication(sys.argv)
    window = Stage2MainWindow()
    window.show()
    app.exec()
