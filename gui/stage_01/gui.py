"""
Stage 1 GUI – Safety Maze
Handles user interface and canvas rendering.
"""

import tkinter as tk
from tkinter import ttk
import csv
from stages.stage_01_core import get_maze_lines
from stages.stage_01_core import trace_beam_path
#-------------------------------------------------------------------------

start_points = { # DEV-2025-22-02 Beam start point maze selection
            "Maze 1 - Straight": (300, 400),
            "Maze 2 - L Shape": (375, 400),
            "Maze 3A - Z Shape": (175, 400),
            "Maze 3B - U Shape": (175, 400),
            "Maze 4A - Snake Shape": (100, 325),
            "Maze 4B - Stair Shape": (150, 325)
        }

# Direction modes: "horizontal" (default) or "vertical"
# DEV-2025-22-05 Stage 1 Fix beam direction orientation
direction_modes = {
    "Maze 1 - Straight": "vertical",
    "Maze 2 - L Shape": "vertical",
    "Maze 3A - Z Shape": "vertical",
    "Maze 3B - U Shape": "vertical",
    "Maze 4A - Snake Shape": "horizontal",
    "Maze 4B - Stair Shape": "horizontal"
}

#-------------------------------------------------------------------------
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
    canvas = tk.Canvas(left_panel, width=620, height=520, bg="white")
    canvas_size = (600, 500)  # Global canvas size for simulation logic
    canvas.pack(fill="both", expand=True)

    # Canvas Grid Lines
    def draw_grid(canvas, size, spacing=50):
        width, height = size
        for x in range(0, width, spacing):
            canvas.create_line(x, 0, x, height, fill="#e0e0e0")
            canvas.create_text(x, 0, text=str(x), anchor="n", font=("Arial", 6), fill="#808080")

        for y in range(0, height, spacing):
            canvas.create_line(0, y, width, y, fill="#e0e0e0")
            canvas.create_text(0, y, text=str(y), anchor="w", font=("Arial", 6), fill="#808080")


    # DEV-2025-22-04 Stage 1 add beam simulation
    # DEV-2025-22-05 Stage 1 Fix beam direction orientation
    #---------------------------------------------------------------------------------
    def update_display():
        """Update maze, starting point, beam path and reflection count."""
        selected = maze_selector.get()
        angle = beam_angle.get()

        if not selected:
            return

        canvas.delete("all")
        draw_grid(canvas, canvas_size)

        # Draw maze walls
        maze_lines = get_maze_lines(selected)
        for (x1, y1), (x2, y2) in maze_lines:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

        # Get orientation and start point
        start = start_points.get(selected, (0, 0))
        orientation = direction_modes.get(selected, "vertical")

        # Run tracer — CSV file will be created
        trace_beam_path(start, angle, maze_lines, canvas_size, orientation)

        # Read from CSV and draw the beam path
        path = []
        with open("results/beam_log.csv", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                path.append((float(row["hit_x"]), float(row["hit_y"])))

        # Insert the starting point at the beginning
        path.insert(0, start)

        # Draw red beam segments
        for i in range(len(path) - 1):
            canvas.create_line(*path[i], *path[i + 1], fill="red", width=2)

        # Draw blue dots at hit points (excluding start and final exit)
        for i in range(1, len(path) - 1):
            rx, ry = path[i]
            canvas.create_oval(rx - 4, ry - 4, rx + 4, ry + 4, fill="blue", outline="white")

        # Draw starting point
        x0, y0 = start
        canvas.create_oval(x0 - 3, y0 - 3, x0 + 3, y0 + 3, fill="green")

        # Set reflection count
        reflection_count = max(0, len(path) - 2)
        reflection_label.config(text=str(reflection_count))

#---------------------------------------------------------------------------------------------------
        # Draw all red beam segments
        for i in range(len(path) - 1):
            canvas.create_line(*path[i], *path[i+1], fill="red", width=2)

        # Draw blue dots at all hit points (excluding start and final exit)
        for i in range(1, len(path) - 1):
            rx, ry = path[i]
            canvas.create_oval(rx - 4, ry - 4, rx + 4, ry + 4, fill="blue", outline="white")

#---------------------------------------------------------------------------------------------------
        # Draw starting point (green)
        x0, y0 = start
        canvas.create_oval(x0 - 3, y0 - 3, x0 + 3, y0 + 3, fill="green")

        # Show reflection count
        reflection_label.config(text=str(reflection_count))

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
        draw_grid(canvas, canvas_size) 

        for line in get_maze_lines(selected):
            canvas.create_line(*line[0], *line[1], width=4)

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

    # DEV-2025-22-04 Stage 1 add beam simulation
    tk.Button(center_controls, text="Simulate Beam", command=update_display).pack(pady=(10, 0))

    # Reflection output
    ttk.Label(center_controls, text="Reflections:",
              font=("TkDefaultFont", 10, "bold")).pack(pady=(20, 10))

    reflection_label = tk.Label(center_controls, text="-")
    reflection_label.pack()


    root.mainloop()
