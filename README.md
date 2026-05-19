# FinalProject

Final project for **Introduction to Programming 2 (Python)**.

## Project Title

**Advanced Calculator System with Operation History**

## Project Description

This project is a Python calculator application with a graphical user interface built with **Tkinter**. The calculator supports both standard and scientific modes. It can perform basic arithmetic operations and advanced mathematical functions such as square root, powers, trigonometric functions, logarithms, factorial, and constants like π and e.

The project follows a modular structure. The code is divided into several Python files, where each file has its own responsibility. This helps make the project easier to understand, test, and improve.

## Project Purpose

The purpose of this project is to create a realistic calculator system that demonstrates Python fundamentals, object-oriented programming, modular architecture, GUI programming, and data management.

The project is more advanced than a basic calculator because it includes:

- standard calculator mode
- scientific calculator mode
- theme settings
- operation handling
- history module
- database module for future saving of operations
- separate files for UI, logic, settings, and data

## Main Features

- graphical user interface using Tkinter
- standard calculator mode
- scientific calculator mode
- second scientific mode with extra functions
- basic operations: addition, subtraction, multiplication, division
- advanced functions: square, cube, square root, cube root, factorial
- trigonometric functions: sin, cos, tan, cot
- logarithmic functions: ln, log, custom base logarithm
- constants: π and e
- power functions: x², x³, xʸ, 10ˣ, 2ˣ, eˣ
- theme changing: Dark, Light, and Blue
- separate history and database modules
- modular project organization

## Technologies Used

- Python
- Tkinter
- Math module
- GitHub
- PostgreSQL

## How the Application Works

1. The user starts the application from `main.py`.
2. The program opens a Tkinter calculator window.
3. The user can use standard calculator buttons.
4. The user can switch between standard and scientific modes using the menu button.
5. The user can use scientific functions such as `sin`, `cos`, `tan`, `ln`, `x²`, `x³`, and others.
6. The user can change the theme using the settings button.
7. The history button is prepared for viewing saved calculations.
8. The database module is prepared for storing and loading operation history.

## Project Structure

```text
Calculator/
├── main.py
├── requirements.txt
├── README.md
├── app/
│   └── calculator.py
├── core/
│   ├── actions.py
│   ├── data.py
│   └── functions.py
├── storage/
│   ├── database.py
│   └── history.py
└── ui/
    ├── components.py
    ├── settings.py
    └── theme.py
```

## File Descriptions

### `Calculator/main.py`

This is the entry point of the program. It creates the main Tkinter window, creates the `Calculator` object, and starts the application loop.

### `Calculator/calculator.py`

This file contains the main `Calculator` class. It controls the calculator window, calculator mode, theme, buttons, settings window, and main user actions.

Main responsibilities:

- create the calculator application
- control standard and scientific modes
- load calculator buttons
- open settings
- change themes
- connect UI with button actions

### `Calculator/actions.py`

This file handles button clicks. It receives the selected button value and decides what action should happen.

Main responsibilities:

- process numbers and operators
- clear the display
- delete one character
- calculate expressions
- handle scientific functions
- handle errors
- use functions from `functions.py`

### `Calculator/functions.py`

This file contains mathematical functions used by the calculator.

Examples:

- `square(x)`
- `cube(x)`
- `inverse(x)`
- `square_root(x)`
- `cube_root(x)`
- `absolute(x)`
- `natural_log(x)`
- `common_log(x)`
- `factorial_num(x)`
- `sine(x)`
- `cosine(x)`
- `tangent(x)`
- `cotangent(x)`

### `Calculator/data.py`

This file stores button layouts for the calculator.

It contains:

- `STANDARD` buttons
- `SCIENTIFIC` buttons
- `SCIENTIFIC_SECOND` buttons

This makes it easier to change the calculator interface without editing the main logic.

### `Calculator/ui.py`

This file creates the graphical interface parts.

Main responsibilities:

- create the header
- create the display
- create the calculator button area

### `Calculator/theme.py`

This file stores color themes.

Available themes:

- `DARK`
- `LIGHT`
- `BLUE`

Each theme contains background color, button color, equal button color, and text color.

### `Calculator/settings.py`

This file stores the current theme setting and includes functions for getting and changing the theme.

### `Calculator/history.py`

This file is responsible for operation history logic.

Main responsibilities:

- add operation to history
- get saved history
- clear history

It works together with `database.py`.

### `Calculator/database.py`

This file is prepared for database operations.

Planned responsibilities:

- connect to the database
- save calculation history
- load saved calculations
- clear saved history

At the current stage, the functions are prepared as placeholders and can be connected to PostgreSQL later.

## UML-Based Design

### Main Classes and Modules

#### `Calculator`

The main class of the project.

Responsibilities:

- starts and controls the calculator
- stores the current mode
- stores the current theme
- loads buttons
- reacts to user actions
- connects UI and logic together

#### `actions.py`

Works as the action controller of the application.

Responsibilities:

- reads button values
- updates the display
- calls mathematical functions
- handles calculation errors

#### `functions.py`

Works as the mathematical service module.

Responsibilities:

- stores reusable math functions
- separates math logic from UI logic
- makes the code cleaner and easier to test

#### `history.py`

Works as the history manager module.

Responsibilities:

- sends history data to the database module
- loads history from the database module
- clears history

#### `database.py`

Works as the database manager module.

Responsibilities:

- save operations
- load operations
- clear operations

## OOP Principles Used

### Encapsulation

The `Calculator` class stores important application data inside one object, such as:

- `root`
- `mode`
- `second_mode`
- `theme`

Methods like `load_buttons()`, `open_menu()`, and `change_theme()` control this data.

### Association

The `Calculator` object works together with functions from other modules:

- `ui.py`
- `actions.py`
- `data.py`
- `theme.py`

This shows association because one part of the program uses another part to complete its work.

### Abstraction

The user only clicks buttons. The user does not need to know how the calculation, theme changing, or UI loading works internally. The internal logic is hidden inside functions and methods.

### Polymorphism

The calculator can work in different modes:

- standard mode
- scientific mode
- second scientific mode

The same button loading method works differently depending on the selected mode.

### Inheritance

Inheritance is not strongly used in the current version. It can be added later by creating a base calculator class and child classes such as:

- `StandardCalculator`
- `ScientificCalculator`

## Data Management

The project includes `history.py` and `database.py` for saving operation history.

Current database functions:

```python
def connect():
    pass

def save(expression, result):
    pass

def load():
    return []

def clear():
    pass
```

These functions are prepared for future PostgreSQL integration. PostgreSQL can be used to save each expression, result, and date of calculation.

Planned database table:

```text
operations
├── id
├── expression
├── result
└── created_at
```

Although the assignment mentions CSV and JSON, this project uses a database module because PostgreSQL is a more structured and realistic way to save operation history.

## Functions and Functional Programming

The project uses many separate functions in `functions.py`. This makes the code modular and reusable.

Examples:

```python
def square(x):
    return x ** 2

def sine(x):
    return sin(radians(x))
```

Functional programming tools can also be added to satisfy the course requirements:

- `lambda`
- `map()`
- `filter()`

Example planned usage:

```python
valid_results = list(filter(lambda x: x is not None, history))
```

## Decorator, Generator, and Regex Plan

To fully satisfy the project requirements, the project can include these features:

### Custom Decorator

A custom decorator can be used to log actions:

```python
def log_action(func):
    def wrapper(*args, **kwargs):
        print("Action started")
        result = func(*args, **kwargs)
        print("Action finished")
        return result
    return wrapper
```

### Generator

A generator can be used to show history step by step:

```python
def history_generator(history):
    for operation in history:
        yield operation
```

### Regex

The `re` module can be used to validate numeric input:

```python
import re

def is_valid_number(value):
    return re.match(r"^-?\d+(\.\d+)?$", value) is not None
```

## Testing Plan

The project should include unit tests using `unittest`.

Planned tests:

- test addition
- test subtraction
- test multiplication
- test division
- test division by zero
- test square function
- test square root function

Suggested test command:

```bash
python -m unittest discover tests
```

## Installation and Running

### 1. Clone the repository

```bash
git clone <repository-link>
```

### 2. Open the project folder

```bash
cd FinalProject-main/Calculator
```

### 3. Run the program

```bash
python main.py
```

## Team Contributions

### Bekzat Amanbek

Responsible for:

- calculator logic
- mathematical functions
- scientific calculator features
- button actions
- OOP structure

### Batyrkhan Uvayev

Responsible for:

- user interface
- theme system
- history module
- database module
- testing, debugging, and integration

## Future Improvements

- connect `database.py` to PostgreSQL
- save every operation automatically
- show operation history in a separate Tkinter window
- add delete-one-operation feature
- add unit tests folder
- add `requirements.txt`
- add input validation with regex
- add decorator for logging actions
- add generator for history display

## Conclusion

This project demonstrates Python fundamentals, modular architecture, object-oriented programming, Tkinter GUI development, mathematical operations, and teamwork. The project already has a working calculator interface and scientific functions. The history and database modules are prepared for further improvement and PostgreSQL integration.
