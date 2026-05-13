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
