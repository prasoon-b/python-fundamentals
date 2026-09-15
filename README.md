# Python Fundamentals

A collection of Python programs written while learning Python fundamentals, one core concept at a time.

## Core Philosophy

Each program focuses on one fundamental concept, building understanding through practice, experimentation, and repetition.
The goal is to develop strong Python fundamentals that become the foundation for more advanced programming, DSA, and AI/ML.

## Content

### Program 1 — `sum_2_num.py`

A beginner-level program that demonstrates how to take numeric input from the user, perform addition, and handle **type casting** in Python.

The program explores two approaches to converting user input from Python's default `string` type into an `integer`:

* **Case 1 — Type casting during input:**
  The `int()` function is applied directly to the result of `input()`. This means the variables `first` and `second` are stored as integers immediately, allowing them to be added directly.

* **Case 2 — Type casting during calculation:**
  The input values are initially stored as strings in `a` and `b`. They are then converted to integers using `int()` when performing the addition. This demonstrates that type conversion does not necessarily have to happen when the input is received.

The program also demonstrates **type casting during output**. Since Python does not allow direct concatenation of a string and an integer using `+`, the calculated integer is converted back to a string using `str()` before being combined with the surrounding text.

Finally, the program demonstrates two ways of printing values:

1. Converting a variable to `str` when concatenating it with another string.
2. Passing the variable directly to `print()`, which allows Python to display the value without manual conversion.

**Core concepts covered:** `input()`, variables, integer type casting with `int()`, string type casting with `str()`, arithmetic operators, string concatenation, and `print()`.
