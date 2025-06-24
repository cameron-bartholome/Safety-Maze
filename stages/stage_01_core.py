"""
Stage 1 Core Logic – Safety Maze
Handles maze presets and related logic for Stage 1.
"""
import math
from shapely.geometry import LineString

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
# DEV-2025-24-02 Trace beam function for beam logic
def trace_beam_path(start, angle_deg, maze_lines, canvas_size, orientation="vertical"):
    if orientation == "vertical":
        angle_deg = 180 - angle_deg
    elif orientation == "horizontal":
        angle_deg = (90 - angle_deg) % 360

    angle_rad = math.radians(angle_deg)
    dx = math.cos(angle_rad)
    dy = -math.sin(angle_rad)

    width, height = canvas_size
    path = [start]
    x, y = start
    max_bounces = 50
    reflections = 0

    for _ in range(max_bounces):
        end = (x + dx * 1000, y + dy * 1000)
        beam_line = LineString([ (x, y), end ])
        closest_hit = None
        closest_wall = None
        closest_dist = float("inf")

        for wall in maze_lines:
            wall_line = LineString(wall)
            if beam_line.intersects(wall_line):
                inter = beam_line.intersection(wall_line)
                if inter.is_empty or not hasattr(inter, 'x'):
                    continue
                px, py = inter.x, inter.y
                dist = (px - x)**2 + (py - y)**2
                if dist < closest_dist:
                    closest_hit = (px, py)
                    closest_wall = wall
                    closest_dist = dist

        if closest_hit:
            # New check: if beam hits *outside* canvas, stop
            if not (0 <= closest_hit[0] <= width and 0 <= closest_hit[1] <= height):
                path.append(closest_hit)
                break
            path.append(closest_hit)
            reflections += 1
            x, y = closest_hit

            # Calculate reflection
            (x1, y1), (x2, y2) = closest_wall
            wall_dx = x2 - x1
            wall_dy = y2 - y1
            wall_length = math.hypot(wall_dx, wall_dy)
            nx = -wall_dy / wall_length
            ny = wall_dx / wall_length
            dot = dx * nx + dy * ny
            dx -= 2 * dot * nx
            dy -= 2 * dot * ny

        else:
            # No hit, beam exits canvas
            out_x = x + dx * 1000
            out_y = y + dy * 1000
            path.append((out_x, out_y))
            break

    return path, reflections
