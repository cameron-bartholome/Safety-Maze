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
    root.geometry("840x500")
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
    control_frame.grid(row=0, column=1, sticky="ns", padx=10)

    #Top Heading: Safety Maze Title
    heading_wrapper = tk.Frame(control_frame)
    heading_wrapper.pack(expand=True)  # Takes vertical space to help center it

    heading_frame = tk.Frame(heading_wrapper)
    heading_frame.pack(pady=(0, 30))

    tk.Label(heading_frame, text="Safety Maze", font=("TkDefaultFont", 14, "bold")).pack()
    tk.Label(heading_frame, text="Stage", font=("TkDefaultFont", 10)).pack(pady=(5, 0))

    stage_box = tk.Label(
        heading_frame, text="1", font=("TkDefaultFont", 18, "bold"),
        width=4, height=2, relief="ridge", borderwidth=2)
    stage_box.pack(pady=(2, 0))

    # Centered inner frame for better layout
    center_controls = tk.Frame(control_frame)
    center_controls.pack(expand=True, pady=(0,30))


    # EVENT HANDLER
    def on_maze_select(_event=None):
        selected = maze_selector.get()
        if not selected:
            return

        canvas.delete("all")

        for line in get_maze_lines(selected):
            canvas.create_line(*line[0], *line[1], width=4)

        start_points = { # DEV-2025-22-02 Beam start point maze selection
            "Maze 1 - Straight": (300, 400),
            "Maze 2 - L Shape": (375, 400),
            "Maze 3A - Z Shape": (175, 400),
            "Maze 3B - U Shape": (175, 400),
            "Maze 4A - Snake Shape": (100, 325),
            "Maze 4B - Stair Shape": (150, 325)
        }

        x, y = start_points.get(selected, (0, 0))
        canvas.create_oval(x-3, y-3, x+3, y+3, fill="red", tags="start")


    # Maze dropdown
    ttk.Label(center_controls, text="Labyrinth Type",
              font=("TkDefaultFont", 10, "bold")).pack(pady=(20, 10))

    maze_selector = ttk.Combobox(center_controls, values=[
        "Maze 1 - Straight", "Maze 2 - L Shape", "Maze 3A - Z Shape",
        "Maze 3B - U Shape", "Maze 4A - Snake Shape", "Maze 4B - Stair Shape"])

    maze_selector.pack()
    maze_selector.bind("<<ComboboxSelected>>", on_maze_select)


    # Beam angle input [DEV-2025-06-22-01 User Input Handling]
    angle_label = tk.Label(center_controls, text="Beam Angle (0° - 180°):",
                           font=("TkDefaultFont", 10, "bold"))

    angle_label.pack(pady=(20, 10))

    beam_angle = tk.IntVar(value=45)

    angle_entry = tk.Entry(center_controls, textvariable=beam_angle, width=5, justify="center")
    angle_entry.pack()

    angle_btn_frame = tk.Frame(center_controls)
    angle_btn_frame.pack(pady=(5, 15))

    tk.Button(angle_btn_frame, text="◀", width=2,
              command=lambda: beam_angle.set(max(0, beam_angle.get() - 1))).pack(side="left")
    tk.Button(angle_btn_frame, text="▶", width=2,
              command=lambda: beam_angle.set(min(180, beam_angle.get() + 1))).pack(side="left")


    # Reflection output
    ttk.Label(center_controls, text="Reflections:",
              font=("TkDefaultFont", 10, "bold")).pack(pady=(20, 10))

    tk.Label(center_controls, text="-").pack()

    root.mainloop()
