"""
launcher.py

DearPyGui-based launcher for the SafetyMaze project.
Displays a GUI to select and launch different stages (e.g., Stage 1: Tkinter, Stage 2: DearPyGui).
This replaces direct execution from main.py and keeps the structure modular.

Linked to: feature/stage2-launcher-setup
"""
#DEV-2025-07-12-01 Stage 2 - Launcher Integration Start

import ctypes  # For screen size (centering)
import importlib
import dearpygui.dearpygui as dpg

def launch_stage(stage_name):
    """
    Closes the launcher GUI and launches the selected stage's GUI.
    """

    # -------------------------- STAGE MODULE PATHS --------------------------

    module_path = {
        "Stage 1": "gui.stage_01.gui",
        "Stage 2": "gui.stage_02.gui", # DEV-2025-07-13-01 Stage 2 - GUI Layout implementation
        # "Stage 3": "gui.stage_03.gui", # Uncomment when stage is ready
    }

    if stage_name in module_path:
        print(f"[INFO] Attempting to import: {module_path[stage_name]}")
        try:
            gui_module = importlib.import_module(module_path[stage_name])
            print("[INFO] Import success. Destroying context and launching stage...")
            dpg.destroy_context()  # Properly shut down launcher before loading next stage
            gui_module.run_gui()
        except Exception as e:
            print(f"[ERROR] Failed to launch {stage_name}: {e.__class__.__name__}: {e}")

def run_launcher():
    """
    Initializes and displays the DearPyGui launcher window with stage selection buttons.
    """
    dpg.create_context()

    # Add font (system default, size 18)
    with dpg.font_registry():
        default_font = dpg.add_font("C:/Windows/Fonts/arial.ttf", 18)

    # Define a custom button theme
    with dpg.theme() as button_theme:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (30, 144, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (65, 105, 225),
                                category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 100, 200),
                                category=dpg.mvThemeCat_Core)

    # -------------------------- MAIN WINDOW --------------------------
    with dpg.window(tag="main_window", label="SafetyMaze Launcher", width=640, height=480):
        dpg.add_text("Select a stage to run:")
        dpg.add_spacer(height=10)

        # ───── Stage 1 Block ─────
        with dpg.group(horizontal=True):
            stage1_btn = dpg.add_button(label="Launch Stage 1", width=120,
                                        callback=lambda: launch_stage("Stage 1"))
            dpg.add_text("Stage 1 - Static Maze\nLaser bounces around fixed labyrinth shapes.",
                            wrap=440)
        dpg.add_spacer(height=20)

        # ───── Stage 2 Block ─────
        with dpg.group(horizontal=True):
            stage2_btn = dpg.add_button(label="Launch Stage 2",
                                        width=120, callback=lambda: launch_stage("Stage 2"),
                                        enabled=True) # make true to turn on stage 2, idiot!
            dpg.add_text("Stage 2 - Dynamic Maze (WIP)\nRebuild of UI using DearPyGui," \
            "interactive setup planned.",
                            wrap=440)

    # -------------------------- VIEWPORT --------------------------
    dpg.create_viewport(title='SafetyMaze Launcher', width=640, height=480)

    # Center viewport on screen
    user32 = ctypes.windll.user32
    screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    x = int((screen_width - 520) / 2)
    y = int((screen_height - 420) / 2)
    dpg.set_viewport_pos([x, y])

    dpg.setup_dearpygui()

    # Apply font and button themes after setup
    dpg.bind_font(default_font)
    dpg.bind_item_theme(stage1_btn, button_theme)
    dpg.bind_item_theme(stage2_btn, button_theme)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
