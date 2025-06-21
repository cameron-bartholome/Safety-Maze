"""
Stage 1 GUI – Safety Maze
Handles user interface and canvas rendering.
"""

import tkinter as tk
from tkinter import ttk
from stages.stage_01_core import get_maze_lines


def run_stage1_gui():
    """Launches the Stage 1 GUI window for the Safety Maze application."""

    root = tk.Tk()
    root.title("Safety Maze Stage 1")
    root.geometry("900x600")
    root.resizable(False, False)

    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

    # Canvas (left)
    left_panel = tk.Frame(main_frame, width=600, height=500, bg="pink")
    left_panel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    canvas = tk.Canvas(left_panel, width=600, height=500, bg="white")
    canvas.pack(fill="both", expand=True)

    # Controls (right)
    control_frame = tk.Frame(main_frame)
    control_frame.grid(row=0, column=1, sticky="n", padx=10)

    # EVENT HANDLER
    def on_maze_select(_event):
        selected = maze_selector.get()
        canvas.delete("all")
        for line in get_maze_lines(selected):
            canvas.create_line(*line[0], *line[1], width=4)

    # Maze dropdown
    ttk.Label(control_frame, text="Labyrinth Type").pack(pady=(0, 5))
    maze_selector = ttk.Combobox(control_frame, values=[
        "Maze 1 - Straight", "Maze 2 - L Shape", "Maze 3A - Z Shape",
        "Maze 3B - U Shape", "Maze 4A - Snake Shape", "Maze 4B - Stair Shape"
    ])
    maze_selector.pack()
    maze_selector.bind("<<ComboboxSelected>>", on_maze_select)

    # Laser input fields
    ttk.Label(control_frame, text="Laser Power").pack(pady=(15, 5))
    tk.Entry(control_frame).pack()

    ttk.Label(control_frame, text="Beam Angle").pack(pady=(15, 5))
    tk.Entry(control_frame).pack()

    # Buttons
    btn_frame = tk.Frame(control_frame)
    btn_frame.pack(pady=20)
    tk.Button(btn_frame, text="Reset").pack(side="left", padx=5)
    tk.Button(btn_frame, text="Run").pack(side="left", padx=5)

    # Reflection output
    ttk.Label(control_frame, text="Reflections:").pack(pady=(10, 0))
    tk.Label(control_frame, text="-").pack()

    root.mainloop()
