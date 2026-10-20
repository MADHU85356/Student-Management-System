# Project Notes

## Purpose
A console-based application for maintaining basic student details.

## Record fields
- `roll`: student roll number (integer)
- `name`: student name (text)
- `branch`: course/department branch (text)

## Main operations
1. Create: add a student record.
2. Read: display or search records.
3. Update: change name, branch, or roll number.
4. Delete: remove a record by roll number.

## Limitation
The application stores data in a Python list in RAM. Data is not saved after the program closes. Persistent CSV or database storage is a possible future enhancement.
