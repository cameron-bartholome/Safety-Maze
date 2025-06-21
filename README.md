# 🧪 Safety Maze – Stage 1: 2D Beam Simulation

## 📌 Overview  
A stage-based Python simulation tool to visualize laser beam paths in 2D labyrinths.  
This first stage focuses on user input, maze preset visualization, and GUI structure using Tkinter.

---

## 🗂️ Folder Structure (Current)

```
safety-maze/
├── main.py
├── gui/
│   └── stage_01/
│       └── gui.py
├── stages/
│   └── stage_01_core.py
├── core/                  # Reserved for shared logic across stages
├── utils/                 # Reserved for helper functions
├── assets/                # Images, diagrams, docs
├── results/               # Logs, output files, future exports
├── tests/                 # Placeholder for future unit testing
└── README.md
```

---

## 🛠️ Features Implemented
- [x] Basic GUI layout with Tkinter
- [x] Maze preset dropdown and canvas rendering
- [x] Modular code split (GUI ↔ logic)
- [x] Stage-based architecture for future upgrades

---

## 🧱 Modules Overview

| File | Purpose |
|------|---------|
| `main.py` | App entry point |
| `gui/stage_01/gui.py` | GUI layout and user input |
| `stages/stage_01_core.py` | Maze presets and logic backend |

---

## ▶️ How to Run
```bash
python main.py
```

---

## 🔜 Planned Next Steps
- [ ] Add beam path simulation (reflection engine)
- [ ] Output images or logs of results
- [ ] Create settings config to load other stages dynamically

---

## 📣 Notes
This project is in development and designed to scale across stages.  
Feel free to explore the layout or adapt the modular structure for your own simulation projects.
