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

### Program 2 — `string_playground.py`

A hands-on exploration of Python's **string manipulation and string-searching capabilities**, using a single string value to demonstrate several commonly used string methods and operators.

The program begins with the string `"Prasoon Bajpai"` and uses it as the basis for experimenting with different operations. Rather than simply performing one task, the program acts as a small **string playground**, demonstrating how Python can inspect, transform, search, and modify string data.

The following concepts are explored:

* **Changing letter case:**
  `name.upper()` converts every alphabetic character in the string to uppercase, while `name.lower()` converts them to lowercase. This demonstrates Python's built-in methods for normalizing or changing the case of text.

* **Finding characters and substrings:**
  `name.find()` is used to locate the position at which a character or substring first appears. The program demonstrates both searching for a single character (`'B'`) and searching for a complete substring (`"Bajpai"`).

* **Handling unsuccessful searches:**
  The program also searches for a character that does not exist in the string (`'z'`). This demonstrates that `find()` returns `-1` when the requested character or substring cannot be found, rather than producing an error.

* **Replacing text:**
  `name.replace("Prasoon", "GOAT")` demonstrates how one portion of a string can be replaced with another string. This introduces Python's string replacement functionality and shows how a modified version of the original string can be produced.

* **Membership testing with `in`:**
  The program uses the `in` operator to check whether specific characters or substrings exist within the string. It tests both individual characters (`'B'`, `'n'`) and a complete substring (`"Bajpai"`), as well as a value that does not exist (`"Ok"`). The result of each membership test is a Boolean value: `True` if the value is present and `False` otherwise.

An important aspect of the program is that it demonstrates that Python's string operations can work with **both individual characters and multiple-character substrings**. It also introduces the distinction between methods that **search or inspect** a string, such as `find()`, and methods that **produce a modified version** of a string, such as `upper()`, `lower()`, and `replace()`.

**Core concepts covered:** strings, string methods, `upper()`, `lower()`, `find()`, `replace()`, the `in` membership operator, Boolean values, character searching, substring searching, string manipulation, and handling unsuccessful searches.

