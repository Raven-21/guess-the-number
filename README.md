# 🎮 Guess the Number

A terminal-based number guessing game built while learning Python.

This project started as a simple script and gradually evolved into a structured software project through continuous refactoring, modular design, and object-oriented programming.

## 🏗️ Current Architecture

The project is now organized into an object-oriented structure:

- main.py → Application controller (game flow)
- game.py → Game object, state management, and game logic
- ui.py → User interface & output
- storage.py → File persistence and storage operations

This architecture separates game logic, presentation, and persistence responsibilities.


## 📚 Project Evolution

### V1 - Modular Architecture

The project was organized into multiple layers:

* data.py → Game state & data processing
* logic.py → Game rules & decision logic
* ui.py → User interface & output
* main.py → Application controller

A centralized `game_state` dictionary was used to manage the entire game state.

### V2 - Object-Oriented Architecture

The project was refactored into a class-based design.

A `Game` class now encapsulates:

* Game state

  * number
  * max_chance
  * history

* Derived properties

  * remaining_chance
  * is_first_try

* Game behaviors

  * add_history()
  * get_stats()
  * check_guess()
  * play_round()

The previous `game_state` dictionary has been replaced by object attributes and methods.

### V2.1 - Persistence Layer

The project now supports file persistence through a dedicated storage layer.

New components:

- storage.py → file operations and data persistence
- game_history.txt → saved game summaries

Game results can now be stored after program execution, introducing basic persistence and file management concepts.

### V2.2 - OOP Refinement

## ✨ Current Features

* Difficulty selection (Easy / Hard)
* Guess history tracking
* Statistics system
* Input validation
* Replay system
* Object-oriented architecture
* Encapsulated game state and logic
* File persistence
* Automatic game summary saving
* Storage layer architecture

## 🧠 Key Design Concepts Practiced

### Separation of Concerns

Each module has a clear responsibility:

* Game Layer → manages game state and game behaviors
* UI Layer → handles presentation and output
* Main Layer → controls application flow


### Object-Oriented Programming (OOP)

The project introduces a dedicated `Game` class:

```python
class Game:
    def __init__(self, max_chance):
        self.number = random.randint(1, 100)
        self.max_chance = max_chance
        self.history = []
```

This allows game state and game behaviors to stay together in a single object.

The Game class now includes both raw state and derived state.

Raw state is stored directly inside the object:

- number
- max_chance
- history

Derived state is calculated dynamically through properties:

- remaining_chance
- is_first_try

### Encapsulation

Game-related data and logic are encapsulated inside the `Game` class.

Examples:

```python
game.play_round(guess)

game.get_stats()

game.remaining_chance

game.is_first_try
```

Instead of passing a centralized state dictionary between multiple functions.


### Software Evolution

This project demonstrates a gradual progression from:

```text
Single Script
    ↓
Functions
    ↓
Modular Design
    ↓
State-Driven Architecture
    ↓
Object-Oriented Design
```


## 🚀 Learning Goals

* Understand real-world project structure
* Practice object-oriented programming in Python
* Learn software architecture fundamentals
* Improve code readability and maintainability
* Transition from scripting → engineering mindset


## 📈 Next Steps

Planned improvements:

* Further refinement of the `Game` class
* Save/load game progress
* Enhanced terminal UI
* Multi-player support
* Data persistence with files