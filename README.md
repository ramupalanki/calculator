# super30-python-package-task-1

## 1. Project Objective

Build a reusable Python package instead of putting all the logic into one Python file.

This project demonstrates the difference between:

- **Function** — a reusable block of code that performs a task.
- **Module** — a Python `.py` file containing related code.
- **Package** — a directory containing related Python modules.
- **Import** — the mechanism used to bring code from another module/package into a Python file.

---

## 2. Project Structure

```text
super30-python-package-task-1/
│
├── calculator_tools/
│   ├── __init__.py
│   ├── arithmetic.py
│   ├── statistics.py
│   ├── converter.py
│   └── exceptions.py
│
└── main.py
```

### What each file does

| File | Purpose |
|---|---|
| `calculator_tools/__init__.py` | Makes `calculator_tools` a package and exposes commonly used functions |
| `calculator_tools/arithmetic.py` | Addition, subtraction, multiplication, division, percentage, and operation selection |
| `calculator_tools/statistics.py` | Average calculation |
| `calculator_tools/converter.py` | Temperature and simple length conversion |
| `calculator_tools/exceptions.py` | Defines the custom `InvalidOperationError` |
| `main.py` | Imports the package and demonstrates all functionality and error handling |

---

# 3. Requirements

You need:

- Python 3 installed
- A terminal/command prompt
- A code editor such as VS Code, PyCharm, or IDLE

No external Python packages are required.

You can check whether Python is installed with:

```bash
python --version
```

If that command does not work, try:

```bash
python3 --version
```

On Windows, you can also try:

```bash
py --version
```

A Python version such as Python 3.10+ is recommended.

---

# 4. Download and Extract the Project

If you received this project as a ZIP file:

1. Download the ZIP file.
2. Extract it to a location on your computer.
3. Open the extracted project folder in your code editor.

Make sure you can see:

```text
calculator_tools/
main.py
README.md
```

inside the project folder.

---

# 5. Open the Terminal in the Correct Folder

The terminal must be opened in the folder containing `main.py`.

For example:

```text
super30-python-package-task-1-updated/
    calculator_tools/
    main.py
    README.md
```

### Windows

In File Explorer:

1. Open the project folder.
2. Click the address bar.
3. Type `cmd`.
4. Press Enter.

Or open the folder in VS Code and choose:

**Terminal → New Terminal**

### Verify the location

Run:

```bash
dir
```

on Windows, or:

```bash
ls
```

on macOS/Linux.

You should see:

```text
calculator_tools
main.py
README.md
```

---

# 6. Run the Complete Project

From the project root folder, run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

On Windows, you can also use:

```bash
py main.py
```

---

# 7. Expected Output

The program demonstrates normal functionality first.

You should see output similar to:

```text
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
20% of 500: 100.0
Average: 25.0
25 C in Fahrenheit: 77.0
77 F in Celsius: 25.0
5000 m in km: 5.0
```

The program then intentionally triggers several errors to demonstrate exception handling.

You should see messages similar to:

```text
Handled division error: Cannot divide by zero.
Handled type error: add() requires numeric values.
Handled value error: Percentage cannot be negative.
Handled custom operation error: Unsupported operation: power
Handled custom conversion error: Unsupported destination unit: yard
```

The exact formatting may vary slightly.

---

# 8. How to Test Each Feature

## Test 1 — Addition

The package provides:

```python
calculator_tools.add(10, 5)
```

Expected result:

```text
15
```

---

## Test 2 — Subtraction

```python
calculator_tools.subtract(10, 5)
```

Expected result:

```text
5
```

---

## Test 3 — Multiplication

```python
calculator_tools.multiply(10, 5)
```

Expected result:

```text
50
```

---

## Test 4 — Division

```python
calculator_tools.divide(10, 5)
```

Expected result:

```text
2.0
```

---

# 9. Test Division by Zero

Try:

```python
calculator_tools.divide(10, 0)
```

The function raises:

```python
ZeroDivisionError
```

`main.py` catches the exception using:

```python
try:
    calculator_tools.divide(10, 0)
except ZeroDivisionError as error:
    print("Handled division error:", error)
```

Expected message:

```text
Handled division error: Cannot divide by zero.
```

---

# 10. Test Incorrect Data Types

Try:

```python
calculator_tools.add("10", 5)
```

The function expects numeric values, but `"10"` is a string.

The function raises:

```python
TypeError
```

Expected message:

```text
Handled type error: add() requires numeric values.
```

---

# 11. Test Percentage Calculation

Example:

```python
calculator_tools.percentage(500, 20)
```

Expected result:

```text
100.0
```

Because:

```text
500 × 20 / 100 = 100
```

---

# 12. Test Invalid Percentage

Try:

```python
calculator_tools.percentage(500, -10)
```

A negative percentage is rejected.

The function raises:

```python
ValueError
```

Expected message:

```text
Handled value error: Percentage cannot be negative.
```

---

# 13. Test Average Calculation

Example:

```python
calculator_tools.average([10, 20, 30, 40])
```

Expected result:

```text
25.0
```

The function calculates the total manually and divides by the number of values.

---

# 14. Test Average with an Empty List

Try:

```python
calculator_tools.average([])
```

This is invalid because an empty list has no average.

The function raises:

```python
ValueError
```

You can test it with:

```python
try:
    calculator_tools.average([])
except ValueError as error:
    print("Handled average error:", error)
```

---

# 15. Test Average with Incorrect Data

Try:

```python
calculator_tools.average([10, 20, "30"])
```

The string `"30"` is not a numeric value.

The function raises:

```python
TypeError
```

---

# 16. Test Temperature Conversion

### Celsius to Fahrenheit

```python
calculator_tools.celsius_to_fahrenheit(25)
```

Expected:

```text
77.0
```

### Fahrenheit to Celsius

```python
calculator_tools.fahrenheit_to_celsius(77)
```

Expected:

```text
25.0
```

---

# 17. Test Temperature with Incorrect Data

Try:

```python
calculator_tools.celsius_to_fahrenheit("25")
```

The function expects a number.

It raises:

```python
TypeError
```

---

# 18. Test Unit Conversion

The project supports simple length conversions involving:

- meters
- kilometers
- centimeters
- miles

Examples:

```python
calculator_tools.convert_units(5000, "m", "km")
```

Expected:

```text
5.0
```

Another example:

```python
calculator_tools.convert_units(10, "km", "mile")
```

This returns approximately:

```text
6.213711922373339
```

---

# 19. Test Unsupported Units

Try:

```python
calculator_tools.convert_units(10, "m", "yard")
```

`yard` is not included in the supported units.

The function raises the custom:

```python
InvalidOperationError
```

Expected message:

```text
Handled custom conversion error: Unsupported destination unit: yard
```

---

# 20. Test the Custom Exception

The project defines its own exception in:

```text
calculator_tools/exceptions.py
```

The exception is:

```python
class InvalidOperationError(Exception):
    """Represent an operation or conversion that is not supported."""
    pass
```

It is used when the requested operation or conversion is not supported.

For example:

```python
calculator_tools.arithmetic.calculate("power", 2, 3)
```

There is no `power` operation in the package, so:

```python
InvalidOperationError
```

is raised.

---

# 21. Test the Operation Selector

The arithmetic module contains:

```python
calculate(operation, a, b)
```

Supported operation names are:

```text
add
subtract
multiply
divide
```

Example:

```python
calculator_tools.arithmetic.calculate("add", 10, 20)
```

Expected:

```text
30
```

Example:

```python
calculator_tools.arithmetic.calculate("multiply", 10, 20)
```

Expected:

```text
200
```

Unsupported operation:

```python
calculator_tools.arithmetic.calculate("power", 2, 3)
```

This raises:

```python
InvalidOperationError
```

---

# 22. Understand the Import

In `main.py`:

```python
import calculator_tools
```

This imports the package.

The functions exposed in `calculator_tools/__init__.py` can then be used like:

```python
calculator_tools.add(10, 5)
```

The custom exception can be imported directly:

```python
from calculator_tools import InvalidOperationError
```

---

# 23. Understand `__init__.py`

The file:

```text
calculator_tools/__init__.py
```

controls what the package exposes.

For example:

```python
from .arithmetic import add, subtract, multiply, divide, percentage
```

makes these functions available through:

```python
calculator_tools.add()
calculator_tools.subtract()
calculator_tools.multiply()
calculator_tools.divide()
calculator_tools.percentage()
```

This demonstrates how multiple modules can work together as one reusable package.

---

# 24. Difference Between Function, Module, Package, and Import

### Function

Example:

```python
def add(a, b):
    return a + b
```

A function performs a specific reusable task.

### Module

Example:

```text
arithmetic.py
```

A module is a Python file containing related code.

### Package

Example:

```text
calculator_tools/
```

A package groups related Python modules together.

### Import

Example:

```python
import calculator_tools
```

Import allows another Python file to use the package's code.

---

# 25. Test the Project from Python

You can also open the Python interpreter from the project root:

```bash
python
```

Then try:

```python
import calculator_tools
```

Test:

```python
calculator_tools.add(100, 50)
```

Expected:

```text
150
```

Test:

```python
calculator_tools.average([10, 20, 30])
```

Expected:

```text
20.0
```

Test:

```python
calculator_tools.celsius_to_fahrenheit(0)
```

Expected:

```text
32.0
```

Exit the Python interpreter with:

```python
exit()
```

---

# 26. Recommended Testing Checklist

Before submitting the project, verify all of the following:

- [ ] Python is installed.
- [ ] The project folder opens correctly.
- [ ] `calculator_tools` exists.
- [ ] `__init__.py` exists.
- [ ] `arithmetic.py` exists.
- [ ] `statistics.py` exists.
- [ ] `converter.py` exists.
- [ ] `exceptions.py` exists.
- [ ] `main.py` exists.
- [ ] `python main.py` runs successfully.
- [ ] Addition works.
- [ ] Subtraction works.
- [ ] Multiplication works.
- [ ] Division works.
- [ ] Division by zero is handled.
- [ ] Percentage calculation works.
- [ ] Invalid percentage is handled.
- [ ] Average calculation works.
- [ ] Empty average input is handled.
- [ ] Incorrect data types are handled.
- [ ] Celsius-to-Fahrenheit works.
- [ ] Fahrenheit-to-Celsius works.
- [ ] Unit conversion works.
- [ ] Unsupported units raise `InvalidOperationError`.
- [ ] Unsupported operations raise `InvalidOperationError`.
- [ ] The package is imported from `main.py`.
- [ ] Functions are separated into logical modules.
- [ ] Custom functions contain docstrings.
- [ ] Comments explain the important code.
- [ ] You understand every line before submitting.

---

# 27. Common Errors and Fixes

## Error: `ModuleNotFoundError: No module named 'calculator_tools'`

Make sure you run:

```bash
python main.py
```

from the **project root**, not from inside the `calculator_tools` folder.

Correct:

```text
super30-python-package-task-1/
├── calculator_tools/
└── main.py
```

Run the command here:

```bash
python main.py
```

---

## Error: `python is not recognized`

Try:

```bash
py --version
```

or:

```bash
python3 --version
```

If Python is not installed, install Python 3 and make sure Python is added to your system PATH.

---

## Error: `ImportError`

Check that:

```text
calculator_tools/
    __init__.py
```

exists and that the spelling of the package and module names is correct.

---

## Error: Permission or file access problem

Make sure the project is extracted to a location where you have permission to create and edit files.

---

# 28. Submission Guidelines

GitHub repository name:

```text
super30-python-package-task-1
```

The repository should contain:

```text
calculator_tools/
    __init__.py
    arithmetic.py
    statistics.py
    converter.py
    exceptions.py

main.py
README.md
```

Do not submit only `main.py`.

The purpose of this task is to demonstrate that the logic has been separated into reusable modules and grouped into a package.

---

# 29. Important Learning Requirement

Do not blindly copy code.

You should be able to explain:

1. What a function is.
2. What a module is.
3. What a package is.
4. What `import` does.
5. Why `__init__.py` is used.
6. Why the arithmetic logic is in `arithmetic.py`.
7. Why average logic is in `statistics.py`.
8. Why conversion logic is in `converter.py`.
9. Why the custom exception is in `exceptions.py`.
10. Why `main.py` imports and demonstrates the package.
11. Why `try` and `except` are used.
12. When `TypeError`, `ValueError`, `ZeroDivisionError`, and `InvalidOperationError` occur.

The goal is not only to make the program run, but to prove that you understand how a reusable Python package is designed.
