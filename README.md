# Library Search Application

This repository contains a library search application that helps users find information about books in a library by subject name, classmark, or location. The application is developed in two parts: a text-based console application and a graphical user interface (GUI) application using Tkinter.

## Table of Contents
- [Part I: Text-Based Console Application](#part-i-text-based-console-application)
- [Part II: Tkinter-Based GUI Application](#part-ii-tkinter-based-gui-application)
- [Common Functionality](#common-functionality)
- [CSV Files](#csv-files)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)

## Part I: Text-Based Console Application

The text-based console application allows users to search for book information by subject name, classmark, or location through the terminal.

### Features
1. Prompt the user to select an option:
   - Search by subject name or part-name
   - Search by classmark
   - Search by location
2. Based on the selection, prompt the user to enter the relevant details.
3. Output the matching classmark along with its location and subject name(s).

### Usage

Run the console application using:
```bash
python library_search_console.py
```

## Part II: Tkinter-Based GUI Application

The Tkinter-based GUI application provides a graphical interface for users to search for book information.

### Features

1. Radio buttons to select the search option:
   - Search by subject name or part-name
   - Search by classmark
   - Search by location
2. Text entry for user input based on the selection.
3. Display the matching classmark along with its location and subject name(s) in a text box.

### Usage

Run the GUI application using:
```bash
python library_search_gui.py
```

## Common Functionality

The common functionality for both applications is encapsulated in library_search_common.py. This module contains functions for reading CSV files, getting locations by classmark, and retrieving subject names by classmark.

### Functions

- read_csv(file_name): Reads data from a CSV file and returns it as a list.
- get_location(classmark, classmarks_data): Returns the location of a given classmark.
- get_subject_names(classmark, subjects_data): Returns a list of subject names for a given classmark.

## CSV Files

The application relies on two CSV files:

1. subjects.csv: Contains a list of subjects and classmarks.
2. locations.csv: Contains a list of classmarks and locations

## How to Run

1. Ensure you have Python installed on your system.
2. Clone the repository:
```bash
git clone https://github.com/yourusername/library-search-app.git
```
3. Navigate to the project directory:
```bash
cd library-search-app
```
4. Ensure you have the required CSV files (subjects.csv and locations.csv) in the project directory.
5. Run the console application:
```bash
python library_search_console.py
```
6. Run the GUI application:
```bash
python library_search_gui.py
```
## Project Structure
```bash
library-search-app/
│
├── library_search_common.py   # Common functionality
├── library_search_console.py  # Console application
├── library_search_gui.py      # GUI application
├── subjects.csv               # Sample subjects data
├── locations.csv              # Sample locations data
└── README.md                  # Project documentation
```