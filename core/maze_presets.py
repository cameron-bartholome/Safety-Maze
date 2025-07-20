"""
Defines maze templates for Stage 2 of the Safety Maze application.

Each maze includes:
- Dimensions with tolerance values (in millimeters)
- Placeholder for 2D geometry (to be calculated separately)

This file is read-only. Do not modify values directly in-place.
User-defined dimensions and geometry modifications should be handled in-memory.

See related dev note in Obsidian: DEV-2025-07-20-02 Stage 2 - Maze Pre-Sets
"""

def get_maze_presets():
    """
    Returns a dictionary of predefined maze presets for Stage 2.

    Each preset includes:
    - 'dimensions': Dict of dimension names with default values and tolerances (in mm).
    - 'geometry': Placeholder list for 2D coordinate paths (to be generated separately).
    """

    # Canvas settings
    canvas_size = (680, 720)  # Width x Height in pixels
    cx, cy = canvas_size[0] // 2, canvas_size[1] // 2  # Center coordinates

    scale_factor = 10  # 1 mm = 10 pixels

    # Set thickness of shapes as 10% of canvas height
    shape_thickness = int(canvas_size[1] * 0.10)  # e.g. 72 pixels

    preset_mazes ={
        # ========== Maze 1 - Straight ==========
        "Maze 1 - Straight": {
            "dimensions": {
                "L1": {"value": 40, "tolerance": 0.2},  # mm
                "G1": {"value": 10, "tolerance": 0.2}   # mm
            },
            # Will be calculated based on dimensions + center
            "geometry": {
                "shapeA": [
                 ((cx-(G1/2), cy-(L1/2)), (cx-(G1/2)-shape_thickness, cy-(L1/2))), # Point 1 to Point 2
                 ((cx-(G1/2)-shape_thickness, cy-(L1/2)), (cx-(G1/2)-shape_thickness, cy+(L1/2))), # Point 2 to Point 3
                 ((cx-(G1/2)-shape_thickness, cy+(L1/2)), (cx-(G1/2), cy+(L1/2))), # Point 3 to Point 4
                 ((cx-(G1/2), cy+(L1/2)), (cx-(G1/2), cy-(L1/2))) # Point 4 to Point 1
                 ],

                 "shapeB": [
                 ((cx+(G1/2)+shape_thickness, cy-(L1/2)), (cx+(G1/2), cy-(L1/2))), # Point 1 to Point 2
                 ((cx+(G1/2), cy-(L1/2)), (cx+(G1/2), cy+(L1/2))), # Point 2 to Point 3
                 ((cx+(G1/2), cy+(L1/2)), (cx+(G1/2)+shape_thickness, cy+(L1/2))), # Point 3 to Point 4
                 ((cx+(G1/2)+shape_thickness, cy+(L1/2)), (cx+(G1/2)+shape_thickness, cy-(L1/2))), # Point 4 to Point 1
                 ]
            }
        }
        # ========== Maze 2 - L Shape ==========
        , "Maze 2 - L Shape": {
            "dimensions": {
                "L1": {"value": 10.0, "tolerance": 0.2},  # mm
                "G1": {"value": 0.5, "tolerance": 0.2},  # mm
                "L2": {"value": 15.0, "tolerance": 0.2},  # mm
                "G2": {"value": 0.7, "tolerance": 0.2}   # mm
            },
            "geometry": []
        }
        # ========== Maze 3A - Z Shape ==========
        , "Maze 3A - Z Shape": {
            "dimensions": {
                "L1": {"value": 10.0, "tolerance": 0.2},  # mm
                "G1": {"value": 0.5, "tolerance": 0.2},  # mm
                "L2": {"value": 15.0, "tolerance": 0.2},  # mm
                "G2": {"value": 0.7, "tolerance": 0.2},  # mm
                "L3": {"value": 20.0, "tolerance": 0.2},  # mm
                "G3": {"value": 1.0, "tolerance": 0.2}    # mm
            },
            "geometry": []
        }
        # ========== Maze 3B - U Shape ==========
        , "Maze 3B - U Shape": {
            "dimensions": {
                "L1": {"value": 10.0, "tolerance": 0.2},  # mm
                "G1": {"value": 0.5, "tolerance": 0.2},  # mm
                "L2": {"value": 15.0, "tolerance": 0.2},  # mm
                "G2": {"value": 0.7, "tolerance": 0.2},  # mm
                "L3": {"value": 20.0, "tolerance": 0.2},  # mm
                "G3": {"value": 1.0, "tolerance": 0.2}    # mm
            },
            "geometry": []
        }
        # ========== Maze 4A - Snake Shape ==========
        , "Maze 4A - Snake Shape": {
            "dimensions": {
                "L1": {"value": 10.0, "tolerance": 0.2},  # mm
                "G1": {"value": 0.5, "tolerance": 0.2},  # mm
                "L2": {"value": 15.0, "tolerance": 0.2},  # mm
                "G2": {"value": 0.7, "tolerance": 0.2},  # mm
                "L3": {"value": 20.0, "tolerance": 0.2},  # mm
                "G3": {"value": 1.0, "tolerance": 0.2},   # mm
                "L4": {"value": 25.0, "tolerance": 0.2},  # mm
                "G4": {"value": 1.2, "tolerance": 0.2},  # mm
                "L5": {"value": 30.0, "tolerance": 0.2},  # mm
                "G5": {"value": 1.5, "tolerance": 0.2}    # mm
            },
            "geometry": []
        }
        # ========== Maze 4B - Stair Shape ==========
        , "Maze 4B - Stair Shape": {
            "dimensions": {
                "L1": {"value": 10.0, "tolerance": 0.2},  # mm
                "G1": {"value": 0.5, "tolerance": 0.2},  # mm
                "L2": {"value": 15.0, "tolerance": 0.2},  # mm
                "G2": {"value": 0.7, "tolerance": 0.2},  # mm
                "L3": {"value": 20.0, "tolerance": 0.2},  # mm
                "G3": {"value": 1.0, "tolerance": 0.2},   # mm
                "L4": {"value": 25.0, "tolerance": 0.2},  # mm
                "G4": {"value": 1.2, "tolerance": 0.2},  # mm
                "L5": {"value": 30.0, "tolerance": 0.2},  # mm
                "G5": {"value": 1.5, "tolerance": 0.2}    # mm
            },
            "geometry": []
        }
    }

    return preset_mazes

