"""
Stage 1 Core Logic – Safety Maze
Handles maze presets and related logic for Stage 1.
"""
import math

# LABYRINTH PRESETS

maze_presets = {
    "Maze 1 - Straight": [ # DEV-2025-22-03 Labyrinth Geometry Update
        ((175, 100), (275, 100)),
        ((325, 100), (425, 100)),
        ((175, 100), (175, 400)),
        ((275, 100), (275, 400)),
        ((325, 100), (325, 400)),
        ((175, 400), (275, 400)),
        ((425, 100), (425, 400)),
        ((325, 400), (425, 400))
    ],
    "Maze 2 - L Shape": [ # DEV-2025-22-03 Labyrinth Geometry Update
        ((150, 50), (150, 100)),
        ((150, 50), (450, 50)),
        ((150, 150), (150, 400)),
        ((150, 100), (400, 100)),
        ((150, 150), (350, 150)),
        ((400, 100), (400, 400)),
        ((350, 150), (350, 400)),
        ((150, 400), (350, 400)),
        ((450, 50), (450, 400)),
        ((400, 400), (450, 400))
    ],
    "Maze 3A - Z Shape": [ # DEV-2025-22-03 Labyrinth Geometry Update
        ((100, 50), (400, 50)),
        ((100, 50), (100, 400)),
        ((450, 50), (500, 50)),
        ((400, 50), (400, 200)),
        ((150, 200), (400, 200)),
        ((150, 200), (150, 400)),
        ((450, 50), (450, 250)),
        ((200, 250), (450, 250)),
        ((200, 250), (200, 400)),
        ((100, 400), (150, 400)),
        ((500, 50), (500, 400)),
        ((200, 400), (500, 400))
    ],
    "Maze 3B - U Shape": [ # DEV-2025-22-03 Labyrinth Geometry Update
        ((100, 400), (150, 400)),
        ((200, 400), (400, 400)),
        ((150, 100), (150, 400)),
        ((150, 100), (450, 100)),
        ((450, 100), (450, 400)),
        ((200, 150), (200, 400)),
        ((200, 150), (400, 150)),
        ((400, 150), (400, 400)),
        ((100, 50), (100, 400)),
        ((100, 50), (500, 50)),
        ((500, 50), (500, 400)),
        ((450, 400), (500, 400))
    ],
    "Maze 4A - Snake Shape": [ # DEV-2025-22-03 Labyrinth Geometry Update
        ((100, 50), (100, 300)),
        ((100, 350), (100, 400)),
        ((100, 300), (200, 300)),
        ((200, 300), (200, 100)),
        ((200, 100), (400, 100)),
        ((400, 100), (400, 300)),
        ((400, 300), (500, 300)),
        ((100, 350), (250, 350)),
        ((250, 350), (250, 150)),
        ((250, 150), (350, 150)),
        ((350, 150), (350, 350)),
        ((350, 350), (500, 350)),
        ((500, 50), (500, 300)),
        ((100, 50), (500, 50)),
        ((100, 400), (500, 400)),
        ((500, 350), (500, 400))
    ],
    "Maze 4B - Stair Shape": [ # DEV-2025-22-03 Labyrinth Geometry Update
        ((150, 50), (150, 300)),
        ((150, 50), (500, 50)),
        ((150, 350), (150, 400)),
        ((150, 300), (250, 300)),
        ((250, 300), (250, 200)),
        ((250, 200), (350, 200)),
        ((350, 200), (350, 100)),
        ((350, 100), (500, 100)),
        ((150, 350), (300, 350)),
        ((300, 350), (300, 250)),
        ((300, 250), (400, 250)),
        ((400, 250), (400, 150)),
        ((400, 150), (500, 150)),
        ((500, 50), (500, 100)),
        ((150, 400), (500, 400)),
        ((500, 150), (500, 400))
    ]
}

def get_maze_lines(maze_name: str):
    """Returns a list of lines for the selected maze preset."""
    return maze_presets.get(maze_name, [])

# DEV-2025-22-04 Stage 1 add beam simulation
def trace_beam_path(start, angle_deg, _maze_lines, _canvas_size, orientation="vertical"):
    """
    Traces the beam from a start point at a given angle,
    reflecting off lines in the maze until it exits the canvas.

    Returns:
        path (list): Points the beam travels through
        reflections (int): Number of times it bounced
    """

    # DEV-2025-06-22-03 Orientation correction
    if orientation == "vertical":
        angle_deg = 180 - angle_deg  # Flip left/right
    elif orientation == "horizontal":
        angle_deg = (90 - angle_deg) % 360  # Flip up/down

    # Convert angle to direction vector
    angle_rad = math.radians(angle_deg)
    dx = math.cos(angle_rad)
    dy = -math.sin(angle_rad)

    # DEV-2025-23-01 Remove beam Logic to start over
    path = [start]

    angle_rad = math.radians(angle_deg)
    dx = math.cos(angle_rad)
    dy = -math.sin(angle_rad)

    # Shoot a long line from the start point
    end_x = start[0] + dx * 1000
    end_y = start[1] + dy * 1000
    path.append((end_x, end_y))

    reflections = 0  # Placeholder, not used yet

    return path, reflections
