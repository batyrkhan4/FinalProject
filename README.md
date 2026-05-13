# FinalProject
Final project for Introduction to Programming 2: calculator system with saved operation history using PostgreSQL.

## Project Description
This project is a Python-based calculator system that performs mathematical operations and stores operation history in a PostgreSQL database. The system is designed using modular architecture and object-oriented programming principles. It allows users to calculate results, save operations, view previous records, and manage stored data through a command-line interface.

## Project Purpose
The purpose of this project is to create a practical calculator application that not only performs calculations, but also stores operation history in a structured database. This makes the system more useful than a basic calculator because users can save, review, and manage previous calculations.

## Main Features
- perform basic operations: addition, subtraction, multiplication, division
- save each operation to PostgreSQL
- view saved operation history
- delete one operation
- clear all operation history
- validate user input
- use a menu-driven command-line interface
  
## Project Workflow
The application follows this logic:

1. The program starts.
2. The calculator menu is displayed.
3. The user chooses one option.
4. If the user selects **Calculate**, the program:
   - asks for the first number
   - asks for the operator
   - asks for the second number
   - validates the input
   - performs the calculation
   - checks division by zero
   - creates an `Operation` object
   - saves the operation using `HistoryManager`
   - displays the result
5. If the user selects **Show History**, the program shows saved operations from the database.
6. If the user selects **Clear History**, the program clears saved history and shows a confirmation message.
7. If the user selects **Exit**, the program ends.

## Technologies Used
- Python
- PostgreSQL
- psycopg2
- GitHub

## Project Structure
```text
FinalProject/
|
|
|- main.py
|- requirements.txt
|- README.md
|- database/
|  |- __init__.py
|  |- db_manager.py
|- models/
|  |- __init__.py
|  |- operation.py
|- services/
|  |- __init__.py
|  |- calculator.py
|  |- history_manager.py
|- ui/
|  |- __init__.py
|  |- menu.py
|- tests/
   |- __init__.py
   |- test_calculator.py
```

## UML-Based Design
### Main Classes
#### CalculatorApp

Responsible for running the program and controlling the menu flow.

Main responsibilities:

start the application
display the main menu
process user choices
connect all modules together
#### Calculator

Responsible for performing mathematical calculations.

Main methods:

add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
#### Operation

Represents one completed mathematical operation.

Main attributes:

num1
operator
num2
result

This class stores one calculation as an object.

#### HistoryManager

Responsible for managing operation history.

Main responsibilities:

add operation to history
show saved history
clear history
work with database manager
#### DatabaseManager

Responsible for PostgreSQL connection and database queries.

Main responsibilities:

connect to PostgreSQL
insert operation into database
fetch saved operations
clear saved operations


## OOP Principles Used

The project demonstrates the following OOP concepts required for the course:

Encapsulation – data and methods are grouped inside classes
Association – HistoryManager works with Operation objects
Abstraction – methods hide internal calculation and database logic
Inheritance – can be extended later through advanced operation classes
Polymorphism – different operation types can be implemented in different ways

## Data Management

The application stores operation history in a PostgreSQL database. This makes data storage more reliable and structured than a simple text file. Each operation is saved as a database record.

Planned Database Table

operations
- id
- num1
- operator
- num2
- result
- created_at

## Functions and Functional Programming

The project also includes modular functions and can use:

keyword and positional arguments
lambda
map()
filter()

These elements support the functional programming part of the project requirements.

## Additional Python Features

To satisfy the project requirements, the system will also include:

regex (re) for input validation
custom decorator for logging actions
iterator or generator for viewing operation history step by step
unit tests using unittest

## Team Contributions
Bekzat Amanbek: Calculator logic, Operation model and OOP structure, User interface and menu system
Batyrkhan Uvayev: DatabaseManager and PostgreSQL integration, Testing, debugging, and integration

## Installation
Clone the repository.

Install dependencies:

```pip install -r requirements.txt```
Create a PostgreSQL database.
Configure database connection settings.

Run the program:

```python main.py```

## Testing

The project includes unit tests to check the correctness of calculations and logic. The goal is to achieve a stable and bug-free runtime with passing tests, as required by the project criteria.

## Conclusion

This project demonstrates Python fundamentals, modular architecture, object-oriented programming, database integration, testing, and teamwork. It is designed as a realistic calculator system that saves operation history and allows the user to manage previous calculations efficiently.
