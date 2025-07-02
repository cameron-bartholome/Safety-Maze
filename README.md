# 🔴 Safety Maze – Laser Reflection Simulator

**Safety Maze** is a visual simulation tool that traces laser beams through a 2D maze and shows how they reflect off surfaces.  
Designed for quick testing, learning, and debugging of beam safety paths using Python + Tkinter.

---

## ✅ Stage 1 – Core Simulation [Completed]

This stage focused on building the basic simulation loop and getting beam reflections working with visual output.

### ✔️ Features Implemented
- [x] Tkinter-based GUI layout
- [x] Prebuilt maze presets with selectable dropdown
- [x] Beam input system (0°–180°)
- [x] Surface-normal reflection logic for realistic beam bouncing
- [x] Nudge system to prevent beam getting stuck at walls
- [x] Logs each beam segment to `results/beam_log.csv`
- [x] CSV includes: start/hit points, angle_in, angle_out
- [x] GUI loads CSV and plots:
  - Red beam lines
  - Blue reflection dots
  - Green start point
- [x] Displays reflection count

📦 Finalized: **2025-07-02**  
📁 Output: `results/beam_log.csv`

## 🖼 Stage 1 Preview

![Stage 1 Beam Simulation Output](assets/stage1-preview.png)

---

## 🧪 Stage 2 – Geometry Expansion [Active]

This stage adds dynamic maze shaping and begins expanding simulation depth.

### 🔧 Planned Features
- [ ] Define maze wall dimensions (gaps, segment length)
- [ ] Support editable labyrinth presets
- [ ] Visualize dimensional changes in the GUI
- [ ] Load/save maze presets from file
- [ ] Add optional surface presets (e.g. anodized aluminum)
- [ ] Support beam width, energy decay per bounce (optional)

---

## 📁 File Structure

```
/gui.py                → GUI logic & visualization
/stage_01_core.py      → Beam tracing logic + reflection system
/results/beam_log.csv  → Simulation output (auto-overwritten)
/maze_presets.py       → Predefined shapes for testing
```

---

## 🚀 Usage

```bash
pip install shapely
python gui.py
```

1. Select a maze preset  
2. Enter a beam angle (0–180°)  
3. Click **Simulate Beam**  
4. View beam path, reflection count, and hit data

---

## 📣 Notes
This project is in development and designed to scale across stages.  
Feel free to explore the layout or adapt the modular structure for your own simulation projects.

---

## 🔒 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License**.

You may share, adapt, or build upon this project **non-commercially**, as long as you give proper credit.  
🔗 [View full license](https://creativecommons.org/licenses/by-nc/4.0/)