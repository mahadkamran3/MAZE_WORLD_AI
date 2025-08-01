# Modern Maze Generator & Solver

A visually stunning maze generation and pathfinding application built with Python and Pygame. This project demonstrates maze generation algorithms and BFS pathfinding with a modern, elegant user interface.

---

## 🚀 Features

- **Dynamic Maze Generation**: Creates random mazes using recursive backtracking algorithm
- **Intelligent Pathfinding**: Solves mazes using Breadth-First Search (BFS) algorithm
- **Modern UI Design**: Clean, dark theme with rounded corners and glow effects
- **Interactive Controls**: Easy-to-use buttons for generating and solving mazes
- **Visual Path Animation**: Animated solution path display
- **Responsive Design**: Smooth hover effects and visual feedback

---

## 🎮 Demo

### Key Functionality:
- Generate unique random mazes
- Visualize the solving process in real-time
- Modern glass-morphism inspired UI
- Smooth animations and transitions

---

## 🗂️ Project Structure

```
AI Project_Code+Doc/
│
├── lab_term.py          # Main application file
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (if needed)
```

---

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- Pygame library

### 1. Clone or Download
```bash
# If using git
git clone <repository-url>
cd "AI Project_Code+Doc"

# Or download the files directly
```

### 2. Install Dependencies
```bash
pip install pygame
```

### 3. Run the Application
```bash
python lab_term.py
```

---

## 🎯 How to Use

1. **Launch the Application**: Run `python lab_term.py`
2. **Generate a New Maze**: Click the "NEW MAZE" button to create a random maze
3. **Solve the Maze**: Click "SOLVE MAZE" to watch the BFS algorithm find the optimal path
4. **Generate Another**: After solving, click "GENERATE NEW" to create a fresh maze
5. **Exit**: Click "QUIT" to close the application

### Controls:
- **NEW MAZE**: Generates a fresh random maze
- **SOLVE MAZE**: Finds and displays the shortest path from start (green) to end (red)
- **GENERATE NEW**: Creates a new maze (available after solving)
- **QUIT**: Exits the application

---

## 🧠 Algorithms Used

### Maze Generation: Recursive Backtracking
- Starts from a random cell
- Randomly chooses unvisited neighbors
- Carves paths by removing walls
- Backtracks when no unvisited neighbors remain
- Guarantees a perfect maze (exactly one path between any two points)

### Pathfinding: Breadth-First Search (BFS)
- Explores all possible paths level by level
- Guarantees finding the shortest path
- Uses a queue to maintain frontier cells
- Tracks parent cells to reconstruct the solution path

---

## 🎨 Technical Features

### Modern UI Components:
- **Rounded Rectangles**: Custom drawing function for modern buttons
- **Glow Effects**: Subtle lighting effects for enhanced visual appeal
- **Color Palette**: Carefully chosen colors for optimal contrast and aesthetics
- **Responsive Buttons**: Hover effects and visual feedback
- **Status Bar**: Real-time information display

### Performance Optimizations:
- Efficient grid representation using 2D arrays
- Optimized drawing routines for smooth 60 FPS
- Smart redraw strategies to minimize computational overhead

---

## 🔧 Configuration

### Customizable Parameters (in code):
```python
WIDTH, HEIGHT = 900, 700    # Window dimensions
ROWS, COLS = 30, 30        # Maze grid size
GRID_SIZE = 500            # Maze display size
```

### Color Scheme:
The application uses a modern dark theme with customizable colors defined in the `COLORS` dictionary.

---

## 📊 Algorithm Complexity

### Maze Generation:
- **Time Complexity**: O(n) where n is the number of cells
- **Space Complexity**: O(n) for the recursion stack

### Pathfinding (BFS):
- **Time Complexity**: O(V + E) where V is vertices and E is edges
- **Space Complexity**: O(V) for the queue and visited set

---

## 🛠️ Technical Requirements

- **Python**: 3.7+
- **Pygame**: 2.0+
- **System**: Windows/macOS/Linux
- **Memory**: ~50MB RAM
- **Display**: Minimum 900x700 resolution

---

## 🎓 Educational Value

This project demonstrates:
- **Data Structures**: 2D arrays, queues, stacks
- **Algorithms**: Recursive backtracking, BFS traversal
- **Game Development**: Pygame fundamentals, event handling
- **UI/UX Design**: Modern interface design principles
- **Software Architecture**: Clean code organization and modularity

---

## 🚧 Future Enhancements

- [ ] Multiple maze generation algorithms (Prim's, Kruskal's)
- [ ] Different pathfinding algorithms (A*, DFS, Dijkstra)
- [ ] Maze size customization from UI
- [ ] Save/load maze functionality
- [ ] Performance metrics display
- [ ] Sound effects and background music
- [ ] Maze export to image files

---

## 🐛 Troubleshooting

### Common Issues:

**Pygame not found**
```bash
pip install pygame
```

**Window doesn't appear**
- Check if your system supports the required resolution
- Ensure graphics drivers are updated

**Performance issues**
- Reduce maze size by modifying `ROWS` and `COLS` values
- Close other resource-intensive applications

---

## 📝 License

This project is created for educational purposes. Feel free to use, modify, and distribute for learning and non-commercial purposes.

---

## 🙏 Acknowledgments

- **Pygame Community**: For the excellent game development library
- **Algorithm Visualizations**: Inspired by various pathfinding visualization tools
- **UI Design**: Modern design principles and color theory

---

## 📞 Contact

Created by: [Your Name]
Course: AI - SEM-5 CUI
Project Type: Lab Terminal Project

For questions or suggestions, please feel free to reach out!

---

## 📚 References

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Maze Generation Algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Python Official Documentation](https://docs.python.org/3/)
