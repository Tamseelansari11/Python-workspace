# Variables

## Overview

A variable is a name used to store data in memory. In Python, you don't need to declare a variable's type explicitly — it is inferred automatically based on the value assigned.

---

## Syntax

```python
variable_name = value
```

- `variable_name` → the name you choose
- `=` → assignment operator (assigns the value on the right to the name on the left)
- `value` → the data being stored

```python
age = 25
```

---

## Visual Explanation

```
    age    =    25
     |           |
     |           |
   variable    value
   (label)    (stored in memory)
```

Think of a variable as a **label tied to a box in memory**, not a box itself:

```
 ┌─────────┐
 │   25    │  <-- memory location
 └─────────┘
      ▲
      │
    age   (label pointing to it)
```

If you reassign the variable, the label just moves to point at a new value:

```python
age = 25   # age -> 25
age = 30   # age -> 30 (old value 25 is discarded)
```

---

## Declaring Variables

```python
name = "Neymar JR"
age = 35
Club = "Barcelona"
goal_average = 1.26
is_player = True
```

Python assigns the type automatically:
- `name` → `str`
- `age` → `int`
- `goal_average` → `float`
- `is_player` → `bool`

---

## Naming Rules

- Must start with a letter or underscore (`_`)
- Cannot start with a number
- Can only contain letters, numbers, and underscores
- Case-sensitive (`age` and `Age` are different variables)
- Cannot use Python reserved keywords (e.g. `class`, `for`, `if`)

**Valid:**
```python
player_name = "mbappe"
_score = 30
total2 = 50
```

**Invalid:**
```python
2total = 50      # cannot start with a number
player-name = "x"  # hyphens not allowed
```

---

## Multiple Assignment

```python
# Assign same value to multiple variables
x = y = z = 0

# Assign different values in one line
a, b, c = 1, 2, 3
```

---

## Reassigning Variables

```python
count = 10
count = count + 1   # count is now 11
count += 1           # count is now 12 (shorthand)
```

---

## Checking Type

```python
x = 10
print(type(x))   # <class 'int'>
```

---

## Common Mistakes (and Fixes)

### 1. Starting a variable name with a number

```python
# Wrong
2total = 50
```
```python
# Correct
total2 = 50
```
Python variable names cannot begin with a digit.

---

### 2. Using hyphens instead of underscores

```python
# Wrong
player-name = "mbappe"
```
```python
# Correct
player_name = "mbappe"
```
Hyphens are read as a minus operator, not part of a name. Use `_` to separate words.

---

### 3. Using spaces in variable names

```python
# Wrong
first name = "Neymar"
```
```python
# Correct
first_name = "Neymar"
```
Spaces break the name into separate tokens and cause a syntax error.

---

### 4. Confusing `=` (assignment) with `==` (comparison)

```python
# Wrong - this assigns, not compares
if age = 18:
    print("Adult")
```
```python
# Correct
if age == 18:
    print("Adult")
```
`=` assigns a value; `==` checks equality.

---

### 5. Using a variable before assigning it a value

```python
# Wrong
print(score)
score = 10
```
```python
# Correct
score = 10
print(score)
```
Python reads top to bottom — a variable must be assigned before it's used.

---

### 6. Using Python reserved keywords as variable names

```python
# Wrong
class = "Math"
```
```python
# Correct
class_name = "Math"
```
Words like `class`, `for`, `if`, `True`, `return` are reserved by Python and can't be used as variable names.

---

### 7. Overwriting built-in function names

```python
# Wrong - this breaks the built-in list() function for the rest of the program
list = [1, 2, 3]
```
```python
# Correct
my_list = [1, 2, 3]
```
Naming a variable `list`, `str`, `sum`, etc. shadows Python's built-in functions.

---

## Key Points

- Variables are created the moment you assign a value.
- Python is dynamically typed — a variable's type can change if reassigned.
- Use descriptive names for readability (`total_price` instead of `tp`).

---

## Practice Questions

### Easy

1. Create a variable `city` and assign it the name of your city. Print it.
2. Create three variables `a`, `b`, `c` in a single line, each holding a different number, using multiple assignment.
3. Assign the value `10` to a variable `x`, then reassign it to `20`. Print `x` after each step.
4. Create a variable `is_raining` and set it to `True` or `False`. Print its type using `type()`.
5. Fix this broken code:
   ```python
   1name = "Sam"
   ```

### Intermediate

1. Create a variable `price` set to `250`. Increase it by `50` using the `+=` shorthand and print the result.
2. Swap the values of two variables `x = 5` and `y = 10` without using a third variable.
3. Create a variable `temperature` and write an `if` statement that checks whether it equals `100`. (Watch out for the `=` vs `==` mistake.)
4. Given `score = "85"` (a string), convert it to an integer and add `10` to it. Print the result and its type.
5. Explain, in your own words, why the following causes an error:
   ```python
   print(total)
   total = 5
   ```

### Advanced

1. Write a short program that starts with `balance = 1000`. Simulate 3 transactions (a deposit and two withdrawals) by reassigning `balance` each time, printing the balance after every transaction.
2. Create variables `a = 5` and `b = 10`. Swap their values using tuple unpacking in one line: `a, b = b, a`. Print both before and after.
3. Given a variable `user_input = "42"`, write code that safely converts it to an integer, and prints an error message instead of crashing if the conversion fails (hint: use `try`/`except`).
4. Without running it, predict the output of the following code and explain why:
   ```python
   x = 5
   y = x
   x = x + 1
   print(x, y)
   ```
5. Write a program that uses multiple assignment to set `a, b, c = 1, 2, 3`, then uses a loop to print each variable name alongside its value (e.g. using a dictionary or `zip`).

---

## Next Module

Proceed to **Data Types** to explore Python's built-in data types in more detail.