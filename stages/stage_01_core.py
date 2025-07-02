"""
Stage 1 Core Logic – Safety Maze
Handles maze presets and related logic for Stage 1.
"""
import math
import csv
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

def trace_beam_path(start, angle_deg, maze_lines,
                    canvas_size, orientation="vertical", max_bounces=50):
    """
    Traces a beam through the maze and logs each segment to CSV.
    Also returns the beam path as a list of points.
    """

    if orientation == "vertical":
        angle_deg = 180 - angle_deg
    elif orientation == "horizontal":
        angle_deg = (90 - angle_deg) % 360

    angle_rad = math.radians(angle_deg)
    dx = math.cos(angle_rad)
    dy = -math.sin(angle_rad)

    width, height = canvas_size
    x, y = start
    path = [start]

    with open("results/beam_log.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["start_x", "start_y", "hit_x", "hit_y", "angle_in", "angle_out"])

        for _ in range(max_bounces):
            end = (x + dx * 1000, y + dy * 1000)
            beam_line = LineString([(x, y), end])
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

            incoming_angle = (math.degrees(math.atan2(-dy, dx))) % 360

            if closest_hit:
                if not (0 <= closest_hit[0] <= width and 0 <= closest_hit[1] <= height):
                    writer.writerow([x, y, closest_hit[0], closest_hit[1], incoming_angle, "EXIT"])
                    path.append(closest_hit)
                    break

                path.append(closest_hit)

                # Reflect beam using proper vector reflection
                (x1, y1), (x2, y2) = closest_wall

                # Wall unit vector
                wall_dx = x2 - x1
                wall_dy = y2 - y1
                wall_length = math.hypot(wall_dx, wall_dy)
                ux = wall_dx / wall_length
                uy = wall_dy / wall_length

                # Surface normal (perpendicular to wall)
                nx = -uy
                ny = ux

                # Reflect the incoming direction
                dot = dx * nx + dy * ny
                dx = dx - 2 * dot * nx
                dy = dy - 2 * dot * ny


                outgoing_angle = (math.degrees(math.atan2(-dy, dx))) % 360
                writer.writerow([x, y, closest_hit[0], closest_hit[1],
                                 incoming_angle, outgoing_angle])

                # Nudge beam slightly forward to escape hit point
                x = closest_hit[0] + dx * 0.001
                y = closest_hit[1] + dy * 0.001

            else:
                out_x = x + dx * 1000
                out_y = y + dy * 1000
                writer.writerow([x, y, out_x, out_y, incoming_angle, "EXIT"])
                path.append((out_x, out_y))
                break

    return path
