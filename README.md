# FinalProject

Final project for **Introduction to Programming 2 (Python)**.

## Project Title

**Advanced Calculator System with PostgreSQL Operation History**

## Project Description

This project is a Python calculator application with a graphical user interface built with **Tkinter**. The calculator supports standard and scientific modes. It can perform arithmetic operations, scientific mathematical functions, change visual themes, save operation history in **PostgreSQL**, show saved history in a separate window, and clear saved history.

The project follows a modular architecture. The code is divided into packages and modules such as `app`, `core`, `storage`, `ui`, and `tests`. This structure makes the project easier to understand, test, maintain, and improve.

## Project Purpose

The purpose of this project is to demonstrate the main topics from Introduction to Programming 2:

- Python fundamentals
- control flow and loops
- functions
- object-oriented programming
- modular architecture
- GUI programming
- PostgreSQL data persistence
- decorators
- generators
- regular expressions
- unit testing
- GitHub collaboration

The project is more advanced than a basic calculator because it saves operation history and separates application logic into clear modules.

## Main Features

- graphical user interface using Tkinter
- standard calculator mode
- scientific calculator mode
- second scientific mode with additional functions
- basic operations: addition, subtraction, multiplication, division
- advanced functions: square, cube, square root, cube root, factorial
- trigonometric functions: sin, cos, tan, cot
- logarithmic functions: ln, common log, custom base logarithm
- constants: π and e
- power functions: x², x³, xʸ, 10ˣ, 2ˣ, eˣ
- theme changing: Dark, Light, and Blue
- PostgreSQL operation history
- history window for saved operations
- clear history button
- custom decorator for action logging
- generator for processing history records
- regex validation for number input
- 15 unit tests using unittest

## Technologies Used

- Python 3
- Tkinter
- PostgreSQL
- psycopg2-binary
- unittest
- re module
- math module
- Git and GitHub

## How the Application Works

1. The user starts the application from `Calculator/main.py`.
2. The program calls `create_table()` and prepares the PostgreSQL table if it does not exist.
3. A Tkinter calculator window opens.
4. The user can use standard calculator buttons.
5. The user can switch between standard and scientific modes using the menu button.
6. The user can use scientific functions such as `sin`, `cos`, `tan`, `ln`, `x²`, `x³`, and others.
7. When the user presses `=`, the result is calculated and saved to PostgreSQL.
8. The user can open the history window using the history button.
9. The history window displays saved operations from the database.
10. The user can clear all saved history.
11. Unit tests can be run from the terminal to check the correctness of the logic.

## Project Structure

```text
FinalProject/
├── README.md
├── requirements.txt
├── .gitignore
└── Calculator/
    ├── main.py
    ├── test_db.py
    ├── app/
    │   ├── __init__.py
    │   └── calculator.py
    ├── core/
    │   ├── __init__.py
    │   ├── actions.py
    │   ├── data.py
    │   ├── decorators.py
    │   ├── functions.py
    │   └── validators.py
    ├── storage/
    │   ├── __init__.py
    │   ├── database.py
    │   └── history.py
    ├── ui/
    │   ├── __init__.py
    │   ├── components.py
    │   ├── settings.py
    │   └── theme.py
    └── tests/
        ├── __init__.py
        └── test_functions.py
```

## File Descriptions

### `Calculator/main.py`

Entry point of the program. It creates the PostgreSQL table, creates the main Tkinter window, creates the `Calculator` object, and starts the application loop.

### `Calculator/app/calculator.py`

Contains the main `Calculator` class. This class controls the application window, current mode, current theme, button loading, settings window, history window, and communication between UI and logic.

Main responsibilities:

- initialize the calculator window
- switch between standard and scientific modes
- load calculator buttons
- open settings window
- change themes
- open history window
- connect button clicks with `core/actions.py`

### `Calculator/core/actions.py`

Handles calculator button clicks. It receives a button value and decides what action should happen.

Main responsibilities:

- process numbers and operators
- clear the display
- delete one character
- calculate expressions
- handle scientific functions
- handle constants π and e
- save completed operations to history
- handle errors
- use the custom `@log_action` decorator

### `Calculator/core/data.py`

Stores button layouts for the calculator.

It contains:

- `STANDARD`
- `SCIENTIFIC`
- `SCIENTIFIC_SECOND`

This makes the interface easier to modify without changing the main calculator logic.

### `Calculator/core/decorators.py`

Contains the custom decorator:

```python
def log_action(func):
```

This decorator logs when an important function is called. It is used to satisfy the custom decorator requirement.

### `Calculator/core/functions.py`

Contains mathematical functions used by the calculator.

Examples:

- `square(x)`
- `cube(x)`
- `inverse(x)`
- `square_root(x)`
- `cube_root(x)`
- `absolute(x)`
- `ten_power(x)`
- `two_power(x)`
- `natural_log(x)`
- `common_log(x)`
- `exponent(x)`
- `factorial_num(x)`
- `sine(x)`
- `cosine(x)`
- `tangent(x)`
- `cotangent(x)`

### `Calculator/core/validators.py`

Contains regex-based validation.

The function:

```python
def is_valid_number(value):
```

uses the `re` module to check whether the user input is a valid integer or decimal number.

### `Calculator/storage/database.py`

Responsible for PostgreSQL connection and database queries.

Main functions:

- `get_connection()`
- `create_table()`
- `save_operation(expression, result)`
- `get_history()`
- `clear_history()`

The database table is created automatically if it does not exist.

### `Calculator/storage/history.py`

Responsible for operation history logic.

Main functions:

- `add_to_history(expression, result)`
- `load_history()`
- `delete_history()`
- `history_generator(records)`

The `history_generator()` function returns history records one by one and satisfies the generator requirement.

### `Calculator/ui/components.py`

Creates the main visual components of the Tkinter interface.

Main responsibilities:

- create header
- create display
- create button frame
- create menu, settings, and history buttons

### `Calculator/ui/theme.py`

Stores available color themes.

Available themes:

- `DARK`
- `LIGHT`
- `BLUE`

Each theme contains background color, button color, equal button color, and text color.

### `Calculator/ui/settings.py`

Stores theme setting helper functions.

### `Calculator/tests/test_functions.py`

Contains unit tests for mathematical functions and regex validation. The project currently has **15 passing tests**.

## Database Design

The project uses PostgreSQL to save operation history.

Database name:

```text
calculator_db
```

Table name:

```text
operations
```

Table structure:

```sql
CREATE TABLE IF NOT EXISTS operations (
    id SERIAL PRIMARY KEY,
    expression TEXT NOT NULL,
    result TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Example record:

```text
id | expression | result | created_at
1  | 2+2        | 4      | 2026-05-20 12:30:00
```

## UML-Based Design

### Main Class: `Calculator`

The `Calculator` class is the main class of the application.

Responsibilities:

- control the Tkinter window
- store current mode
- store current theme
- load calculator buttons
- open settings window
- open history window
- send button values to action logic

### Supporting Modules

#### `core/actions.py`

Responsible for processing button clicks and connecting UI actions with calculator functions.

#### `core/functions.py`

Responsible for mathematical calculations.

#### `storage/database.py`

Responsible for direct PostgreSQL operations.

#### `storage/history.py`

Responsible for history management and generator logic.

#### `ui/components.py`

Responsible for creating the visual interface.

## OOP Principles Used

### Encapsulation

The `Calculator` class stores related data and behavior together, such as mode, theme, display, buttons, and windows.

### Abstraction

Complex actions such as calculation, saving history, and database connection are hidden inside functions and modules. The user only interacts with buttons.

### Association

The `Calculator` class works together with UI modules, action modules, and history modules. For example, the calculator calls `handle_click()`, and history functions call database functions.

### Polymorphism

The calculator can process different button values in different ways. For example, numeric buttons, arithmetic operators, scientific functions, and special buttons all use the same click flow but produce different behavior.

### Inheritance

The project uses Tkinter classes such as `Tk`, `Toplevel`, `Frame`, `Button`, `Entry`, and `Text`. These are object-oriented GUI components provided by the Tkinter library. The project can also be extended in the future with inherited calculator classes such as `BasicCalculator` and `ScientificCalculator`.

## Functional Programming Elements

The project uses functions to separate logic into reusable parts. Examples include mathematical functions in `core/functions.py`, database functions in `storage/database.py`, and validation functions in `core/validators.py`.

The project can also use lambda expressions in button commands, for example:

```python
command=lambda t=text: self.click(t)
```

This allows each button to send its own value to the click handler.

## Decorator

The project includes a custom decorator in `core/decorators.py`:

```python
@log_action
```

It logs when the button handling function is called. This satisfies the decorator requirement.

## Generator

The project includes a generator in `storage/history.py`:

```python
def history_generator(records):
    for record in records:
        yield record
```

It is used to process saved history records one by one in the history window.

## Regex Validation

The project includes regex validation in `core/validators.py`:

```python
pattern = r"^-?\d+(\.\d+)?$"
```

This checks whether a value is a valid number.

## Unit Testing

The project uses `unittest` and includes tests in:

```text
Calculator/tests/test_functions.py
```

The tests check:

- square
- cube
- inverse
- square root
- cube root
- absolute value
- powers
- logarithms
- exponent
- factorial
- sine
- cosine
- regex validation

Run tests from the `Calculator` directory:

```bash
python -m unittest discover -s tests -t . -p "test_*.py" -v
```

Expected result:

```text
Ran 15 tests
OK
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/batyrkhan4/FinalProject.git
cd FinalProject/Calculator
```

### 2. Install dependencies

```bash
pip install -r ../requirements.txt
```

If you are already in the repository root, use:

```bash
pip install -r requirements.txt
```

### 3. Create PostgreSQL database

Open pgAdmin or PostgreSQL terminal and run:

```sql
CREATE DATABASE calculator_db;
```

The `operations` table is created automatically when the program starts.

### 4. Configure database connection

Open:

```text
Calculator/storage/database.py
```

Check these values:

```python
DB_NAME = "calculator_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
```

If your PostgreSQL password is different, change `DB_PASSWORD`.

### 5. Run the application

From the `Calculator` directory:

```bash
python main.py
```

## GitHub Workflow

Before starting work:

```bash
git pull
```

After changing files:

```bash
git status
git add .
git commit -m "Update project"
git push
```

## Team Contributions

### Bekzat Amanbek

- calculator logic
- mathematical functions
- operation handling
- scientific calculator mode
- OOP structure
- user interface improvements

### Batyrkhan Uvayev

- modular project structure
- PostgreSQL integration
- operation history
- history window
- clear history functionality
- decorator, generator, regex validation
- unit tests
- README and GitHub integration

## Quality Assurance

The project includes:

- modular package structure with `__init__.py`
- unit tests
- PostgreSQL persistence
- error handling in calculation actions
- separate responsibilities for each module
- readable function names
- GitHub version control

## Future Improvements

Possible future improvements:

- add user accounts
- add delete-one-history-record feature
- add export history to CSV
- improve validation before using `eval()`
- add more unit tests for database functions
- add more advanced scientific functions
- hide database password using `.env` file

## Conclusion

This project demonstrates Python fundamentals, GUI programming, modular architecture, object-oriented programming, PostgreSQL database integration, testing, decorators, generators, regex validation, and teamwork. It is a realistic calculator system that saves operation history and allows users to manage previous calculations efficiently.
