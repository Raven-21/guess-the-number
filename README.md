# 🎮 Guess the Number

A terminal-based number guessing game built while learning Python.

This project started as a simple script and gradually evolved into a structured multi-file application through continuous refactoring and software design improvements.

## 🏗️ Current Architecture

The project is now organized into a modular structure:

- main.py → Application controller (game flow)
- data.py → Game state & data processing
- logic.py → Game rules & decision logic
- ui.py → User interface & output

This marks the transition from a single-script program to a modular software design.


## ✨ Current Features

- Difficulty selection (Easy / Hard)
- Guess history tracking
- Statistics system
- Input validation
- Modular architecture (multi-file structure)
- State-driven design using `game_state`


## 🧠 Key Design Concepts Practiced

### Separation of Concerns
Each module has a clear responsibility:

- Data layer → manages game state
- Logic layer → handles game rules
- UI layer → handles output
- Main layer → controls flow


### State Management

The game uses a centralized state object:

```python
game_state = {
    "number": 42,
    "max_chance": 10,
    "history": []
}
```

This reduces complexity and avoids scattered variables.

### Modular Design

The project now demonstrates:

- Multi-file organization
- Explicit imports between modules
- Clear dependency direction
- Improved maintainability

## 🚀 Learning Goals

- Understand real-world project structure
- Practice modular programming in Python
- Learn software architecture fundamentals
- Improve code readability and maintainability
- Transition from scripting → engineering mindset

## 📈 Next Steps

Planned improvements:

- Further refactoring of `main.py` into a cleaner controller
- Optional OOP (Class-based design)
- Save/load game progress
- Enhanced terminal UI