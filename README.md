# Student Management System

A beginner-friendly, console-based mini project built with Python. It manages student records through a menu-driven interface.

## Features
- Add a student (roll number, name, and branch)
- Display all student records
- Search by roll number
- Update a student's name, branch, or roll number
- Delete a student record
- Basic input validation and duplicate roll-number checking

## Technology
- Python 3
- Built-in Python data structures (list and dictionary)

## Requirements
Python 3.8 or later. No third-party packages are required.

## Run the project
1. Install Python 3 from https://www.python.org/downloads/
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python student_management.py
   ```

   On some Windows installations, use `py student_management.py`.

## Important limitation
This version stores records in memory while the program is running. Records are cleared when the program exits. CSV or database storage can be added as a future enhancement.

## Project structure
```text
Student-Management-System/
├── student_management.py
├── README.md
├── requirements.txt
├── .gitignore
├── PROJECT_REPORT.pdf
└── tests/
    └── test_student_management.py
```

## Mini project
This repository supports the Student Management System mini-project report. The included Python implementation has input checks and duplicate-roll validation in addition to the basic features described in the report.
