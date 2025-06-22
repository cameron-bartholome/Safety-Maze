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
    path = [start]
    reflections = 0

    # DEV-2025-06-22-03 Orientation correction
    if orientation == "vertical":
        angle_deg = 180 - angle_deg  # Flip left/right
    elif orientation == "horizontal":
        angle_deg = (90 - angle_deg) % 360  # Flip up/down

    # Convert angle to direction vector
    angle_rad = math.radians(angle_deg)
    dx = math.cos(angle_rad)
    dy = -math.sin(angle_rad)

    # DEV-2025-22-06 Stage 1 Fix false reflection count when laser goes off-screen
    x, y = start
    max_bounces = 100  # safety limit
    while 0 <= x <= _canvas_size[0] and 0 <= y <= _canvas_size[1] and reflections < max_bounces:
        next_x = x + dx * 5
        next_y = y + dy * 5

        hit = False
        for wall in _maze_lines:
            (x1, y1), (x2, y2) = wall
            denom = (x2 - x1) * (y - next_y) - (y2 - y1) * (x - next_x)
            if denom == 0:
                continue  # parallel

            ua = ((x2 - x1) * (y1 - y) - (y2 - y1) * (x1 - x)) / denom
            ub = ((next_x - x) * (y1 - y) - (next_y - y) * (x1 - x)) / denom

            if 0 <= ua <= 1 and 0 <= ub <= 1:
                ix = x + ua * (next_x - x)
                iy = y + ua * (next_y - y)
                path.append((ix, iy))
                reflections += 1

                wall_dx = x2 - x1
                wall_dy = y2 - y1
                length = math.hypot(wall_dx, wall_dy)
                nx = -wall_dy / length
                ny = wall_dx / length
                dot = dx * nx + dy * ny
                dx -= 2 * dot * nx
                dy -= 2 * dot * ny

                x, y = ix, iy
                hit = True
                break

        if hit:
            continue  # Already updated x, y and path when hitting wall
        else:
            # Only append the last point when it exits the canvas
            x = next_x
            y = next_y
            if 0 <= x <= _canvas_size[0] and 0 <= y <= _canvas_size[1]:
                path.append((x, y))


    return path, reflections
