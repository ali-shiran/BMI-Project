# BMI-Project
BMI project built with puthon

BMI Calculator (Version 1.0)

Overview

This project is a console-based BMI (Body Mass Index) calculator written in Python.

The primary goal of this project was not to build the most advanced BMI calculator, but to learn how to design and implement a real-world Python application using functional programming principles.

Instead of solving isolated exercises, this project focuses on creating a complete application that collects user information, validates inputs, calculates BMI, stores user data, and saves it for future use.

---

Features

- Collects user information:
  
  - First Name
  - Last Name
  - Age
  - Gender
  - Measurement System (Metric / Imperial)
  - Height
  - Weight

- Supports both Metric and Imperial measurement systems.

- Automatically converts Imperial values to Metric for standardized storage.

- Calculates:
  
  - BMI Score
  - BMI Category

- Allows users to review and edit their information before saving.

- Automatically assigns a unique ID to every new user.

- Saves user data into a CSV file.

- Reads previously saved IDs to continue numbering correctly between program runs.

---

Technologies

- Python 3
- csv module
- os module

---

Project Structure

The project is organized into multiple functions, each responsible for a single task whenever possible.

Examples include:

- Building user data
- Input validation
- Unit conversion
- BMI calculation
- Data management
- CSV preparation
- CSV saving

This structure was intentionally chosen to prepare for Object-Oriented Programming in Version 2.

---

Data Stored

Each user is saved with the following information:

- ID
- First Name
- Last Name
- Age
- Gender
- Measurement System
- Height (Meters)
- Weight (Kilograms)
- BMI Score
- BMI Status

Only processed (standardized) data is stored in the CSV file to simplify future analysis.

---

Learning Goals

This project was created to practice:

- Functional Programming
- Program Design
- Separation of Responsibilities
- Data Validation
- Working with Dictionaries
- Nested Data Structures
- Reading and Writing CSV Files
- File Handling
- Debugging
- Modular Thinking

---

Future Plans (Version 2)

Version 2 will focus on learning new technologies rather than expanding the console application.

Planned improvements include:

- Object-Oriented Programming
- User class
- SQLite Database
- Django Backend
- Simple Web Interface
- Improved Data Management

---

Lessons Learned

This project taught me that writing software is much more than making code work.

Throughout development I learned how to:

- Break large problems into smaller functions.
- Design program flow before writing code.
- Think about responsibility and ownership of functions.
- Separate data collection, processing, and storage.
- Debug logical problems instead of only syntax errors.
- Build software that is easier to maintain and extend.

---

Repository Purpose

This repository represents an important milestone in my journey toward becoming a Data Scientist and Backend Developer.

Rather than following tutorials only, I chose to build practical projects that gradually introduce more advanced software engineering concepts.

This project serves as the foundation for future versions that will use Object-Oriented Programming, databases, and web technologies.

What I would improve if I rebuilt this project today:
Replace dictionaries with classes.

Use SQLite instead of CSV.

Build a web interface with Django.

Improve the user experience.

Add automated tests.
