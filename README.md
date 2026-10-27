# 🐍 Advanced Python Programming (APP)

> **Advance Python assignments for SY [SEM - III]**

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Course](https://img.shields.io/badge/Course-Advance%20Python%20Programming-orange?logo=book&logoColor=white)](#)
[![Libraries](https://img.shields.io/badge/Libraries-NumPy%20%7C%20Pandas%20%7C%20Matplotlib-brightgreen?logo=pandas&logoColor=white)](#)

This repository contains a comprehensive collection of Advanced Python assignments focused on core Python concepts, Object-Oriented Programming (OOP), Dynamic Programming algorithms, File Handling, Data Analysis (NumPy & Pandas), and standard Software Design Patterns.

---

## 📑 Table of Contents

- [📚 Core Assignments (0 – 12)](#-core-assignments)
  - [Assignment 0: Function Arguments](#assignment-0-function-arguments)
  - [Assignment 1: Library Management System (OOP)](#assignment-1-library-management-system-oop)
  - [Assignment 2: Dynamic Report Generator](#assignment-2-dynamic-report-generator)
  - [Assignment 3: Configurable Payment Processing System](#assignment-3-configurable-payment-processing-system)
  - [Assignment 4: Memoization & Tabulation](#assignment-4-memoization--tabulation)
  - [Assignment 5: Longest Common Subsequence (LCS)](#assignment-5-longest-common-subsequence-lcs)
  - [Assignment 6: 0/1 Knapsack Problem](#assignment-6-01-knapsack-problem)
  - [Assignment 7: Regex Email Pattern Finder](#assignment-7-regex-email-pattern-finder)
  - [Assignment 8: File I/O & Line Counting](#assignment-8-file-io--line-counting)
  - [Assignment 9: CSV to JSON Converter](#assignment-9-csv-to-json-converter)
  - [Assignment 10: NumPy Array Operations & Broadcasting](#assignment-10-numpy-array-operations--broadcasting)
  - [Assignment 11: Pandas Series & Statistical Operations](#assignment-11-pandas-series--statistical-operations)
  - [Assignment 12: Exploratory Data Analysis (EDA) on Customer Churn](#assignment-12-exploratory-data-analysis-eda-on-customer-churn)
- [📐 Design Patterns Assignments](#-design-patterns-assignments)
  - [1. Singleton Pattern](#1-singleton-pattern)
  - [2. Factory Pattern](#2-factory-pattern)
  - [3. Observer Pattern](#3-observer-pattern)
- [📦 Requirements & Dependency Matrix](#-requirements--dependency-matrix)
- [📁 Repository Structure](#-repository-structure)
- [🚀 Getting Started & Installation Guidelines](#-getting-started--installation-guidelines)

---

## 📚 Core Assignments

### [Assignment 0: Function Arguments](Assignment_0.py)

Develop a Python program that demonstrates the use of **required**, **keyword**, **default**, and **variable-length** (`*args` and `**kwargs`) arguments through functions.

### [Assignment 1: Library Management System (OOP)](Assignment_1.py)

Write a program to create a simplified **Library Management System** using object-oriented programming principles in Python. This system should manage books and patrons (library users), allowing for basic operations such as:

- Adding new books
- Registering patrons
- Borrowing books
- Returning books

### [Assignment 2: Dynamic Report Generator](Assignment_2.py)

Design a dynamic report generator in Python that utilizes **decorators**, **class methods**, and **magic methods** to customize and format reports. The system should allow users to define report templates and apply various formatting options dynamically.

### [Assignment 3: Configurable Payment Processing System](Assignment_3.py)

Write a program to implement a Configurable Payment Processing System utilizing the **Strategy Pattern**.

### [Assignment 4: Memoization & Tabulation](Assignment_4.py)

Write a program to understand and implement dynamic programming concepts, specifically **Memoization** and **Tabulation**.

### [Assignment 5: Longest Common Subsequence (LCS)](Assignment_5.py)

Apply **Dynamic Programming** to Find the **Longest Common Subsequence (LCS)**.

### [Assignment 6: 0/1 Knapsack Problem](Assignment_6.py)

Write a code for optimal selection of items to maximize value within a weight constraint using **bottom-up** and **top-down** approaches using the **dynamic programming** approach.

### [Assignment 7: Regex Email Pattern Finder](Assignment_7.py)

Write a Python script using **regular expressions (regex)** to find email patterns.

### [Assignment 8: File I/O & Line Counting](Assignment_8.py)

Create a Python script to read data from an input file. Perform line counting, extract the first two lines, and write the extracted data into a new file.

### [Assignment 9: CSV to JSON Converter](Assignment_9.py)

Develop a Python script to read data from a CSV file, convert it into JSON format, and store the converted data in a JSON output file.

### [Assignment 10: NumPy Array Operations & Broadcasting](Assignment_10.py)

Apply **NumPy** to create a one-dimensional array containing the numbers from 1 to 10, perform slicing operations, compute statistical measures (sum, mean, maximum, and minimum), and apply broadcasting to modify the array elements.

### [Assignment 11: Pandas Series & Statistical Operations](Assignment_11.py)

Apply **Pandas** to create a Series containing ten random numbers and perform indexing, filtering, and statistical operations such as mean, median, minimum, and maximum.

### [Assignment 12: Exploratory Data Analysis (EDA) on Customer Churn](Assignment_12.py)

Apply **NumPy** and **Pandas** to perform exploratory data analysis (EDA) on a customer churn dataset by cleaning the data, handling missing values, generating summary statistics, and identifying significant patterns through visualization.

---

## 📐 Design Patterns Assignments

This section focuses on implementing standard software design patterns in Python:

- **[1. Singleton Pattern](Design_Pattern-Singleton_Pattern.py):**
  Create a `Printer` class. Multiple users should access the same printer object to print documents. Verify that only one object of this class exists in memory.

- **[2. Factory Pattern](Design_Pattern-Factory_Pattern.py):**
  Create a `FruitFactory` that returns `Apple`, `Mango`, or `Orange` objects. Each fruit class should have a method to display its name.

- **[3. Observer Pattern](Design_Pattern-Observer_Pattern.py):**
  Develop a `Weather Station` that automatically notifies all registered display devices (observers) whenever the temperature changes.

---

## 📦 Requirements & Dependency Matrix

The assignments in this repository range from pure standard library scripts to data science tasks requiring external libraries. Below is the dependency breakdown:

| Assignment          | Topic                                    | External Dependencies           | Standard Library Modules | Installation Needed?                  |
| :------------------ | :--------------------------------------- | :------------------------------ | :----------------------- | :------------------------------------ |
| **Assignment 0**    | Function Arguments (`*args`, `**kwargs`) | _None_                          | Built-in                 | ❌ None (Standard Library)            |
| **Assignment 1**    | Library Management System (OOP)          | _None_                          | Built-in                 | ❌ None (Standard Library)            |
| **Assignment 2**    | Dynamic Report Generator (Decorators)    | _None_                          | Built-in                 | ❌ None (Standard Library)            |
| **Assignment 3**    | Payment Processing System (Strategy)     | _None_                          | `abc`                    | ❌ None (Standard Library)            |
| **Assignment 4**    | Memoization & Tabulation                 | _None_                          | Built-in                 | ❌ None (Standard Library)            |
| **Assignment 5**    | Longest Common Subsequence (LCS)         | _None_                          | Built-in                 | ❌ None (Standard Library)            |
| **Assignment 6**    | 0/1 Knapsack Problem (DP)                | _None_                          | Built-in                 | ❌ None (Standard Library)            |
| **Assignment 7**    | Regex Email Matching                     | _None_                          | `re`                     | ❌ None (Standard Library)            |
| **Assignment 8**    | File Reading & Line Extraction           | _None_                          | Built-in (`open`)        | ❌ None (Standard Library)            |
| **Assignment 9**    | CSV to JSON Converter                    | _None_                          | `csv`, `json`            | ❌ None (Standard Library)            |
| **Assignment 10**   | Array Slicing & Broadcasting             | `numpy`                         | Built-in                 | `pip install numpy`                   |
| **Assignment 11**   | Series Filtering & Statistics            | `pandas`, `numpy`               | Built-in                 | `pip install pandas numpy`            |
| **Assignment 12**   | EDA & Churn Analysis Visualization       | `pandas`, `numpy`, `matplotlib` | Built-in                 | `pip install pandas numpy matplotlib` |
| **Design Patterns** | Singleton, Factory, Observer             | _None_                          | Built-in                 | ❌ None (Standard Library)            |

---

## 📁 Repository Structure

```text
├── Assignment_0.py                         # Function Arguments (*args, **kwargs)
├── Assignment_1.py                         # Library Management System (OOP)
├── Assignment_2.py                         # Dynamic Report Generator (Decorators)
├── Assignment_3.py                         # Payment Processing System (Strategy Pattern)
├── Assignment_4.py                         # Memoization & Tabulation (Fibonacci)
├── Assignment_5.py                         # Longest Common Subsequence (LCS)
├── Assignment_6.py                         # Knapsack Problem (DP Bottom-Up & Top-Down)
├── Assignment_7.py                         # Regular Expressions (Email Finder)
├── Assignment_8.py                         # File I/O, Line Counting & Extraction
├── Assignment_9.py                         # CSV to JSON Data Converter
├── Assignment_10.py                        # NumPy Array Operations & Broadcasting
├── Assignment_11.py                        # Pandas Series & Statistical Operations
├── Assignment_12.py                        # EDA & Customer Churn Analysis (Pandas & Matplotlib)
├── Design_Pattern-Singleton_Pattern.py     # Singleton Pattern
├── Design_Pattern-Factory_Pattern.py       # Factory Method Pattern
├── Design_Pattern-Observer_Pattern.py      # Observer Pattern
├── assignment_8_input.txt                  # Input data for Assignment 8
├── assignment_8_output.txt                 # Extracted output for Assignment 8
├── assignment_9_input.csv                  # Sample CSV input for Assignment 9
├── assignment_9_output.json                # Generated JSON output for Assignment 9
└── requirements.txt                        # Third-party dependencies specification
```

---

## 🚀 Getting Started & Installation Guidelines

### 1. Prerequisites

- **Python 3.10 or higher** installed on your system.
- Check your current Python version:
  ```bash
  python --version
  ```

---

### 2. Virtual Environment Setup (Recommended)

It is recommended to set up an isolated virtual environment to manage external libraries cleanly.

#### Windows (PowerShell):

```powershell
# Create a virtual environment named .venv
python -m venv .venv

# Activate the virtual environment
.venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt):

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

#### macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Dependency Installation Guidelines

#### Option A: Install All Dependencies at Once (Recommended)

Install all required libraries using the included [requirements.txt](requirements.txt):

```bash
pip install -r requirements.txt
```

#### Option B: Install Selective Dependencies per Assignment

If you only wish to run specific assignments, install only the relevant packages:

- **For Assignment 10 (NumPy):**

  ```bash
  pip install numpy
  ```

- **For Assignment 11 (Pandas & NumPy):**

  ```bash
  pip install pandas numpy
  ```

- **For Assignment 12 (Pandas, NumPy & Matplotlib):**
  ```bash
  pip install pandas numpy matplotlib
  ```

---

### 4. Verify Installation

To verify that all external libraries are properly installed and accessible:

```bash
python -c "import numpy, pandas, matplotlib; print(' All dependencies installed successfully!')"
```

---

### 5. Running the Assignments

Run any assignment or design pattern script directly from the project root:

```bash
# Example 1: Run core OOP assignment
python Assignment_1.py

# Example 2: Run dynamic programming knapsack problem
python Assignment_6.py

# Example 3: Run regex pattern finder (prompts for input text)
python Assignment_7.py

# Example 4: Run NumPy array operations
python Assignment_10.py

# Example 5: Run Customer Churn EDA & Visualization
python Assignment_12.py

# Example 6: Run Singleton Design Pattern
python Design_Pattern-Singleton_Pattern.py
```
