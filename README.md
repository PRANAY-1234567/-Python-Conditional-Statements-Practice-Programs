# 🐍 Python Conditional Statements – Practice Programs

A collection of beginner-friendly **Python conditional statement programs** designed to practice decision-making, comparison operators, logical operators, arithmetic operations, strings, tuples, and nested conditions.

These programs cover practical examples such as checking divisibility, classifying numbers, validating login credentials, determining student grades, and making decisions based on battery percentage and available money.

---

## 📌 Overview

This repository contains **10 Python practice programs** based mainly on:

* `if` statements
* `if-elif-else`
* Comparison operators
* Logical operators
* Arithmetic operators
* String operations
* `isinstance()`
* Tuples
* Number classification
* Basic input validation
* Decision-making logic

The programs are suitable for beginners who are learning Python fundamentals and conditional statements.

---

# 📂 Project Structure

```text
Python-Conditional-Practice/
│
├── 01_divisibility_check.py
├── 03_string_length.py
├── 04_string_tuple_check.py
├── 05_age_category.py
├── 06_smallest_of_three.py
├── 07_marks_grade.py
├── 08_login_validation.py
├── 09_number_classification.py
├── 10_trip_decision.py
└── README.md
```

> **Note:** Your provided collection starts from 1 and then continues with 3–10. Program 2 was not included in the provided code.

---

# 1️⃣ Divisibility Check

### 📌 Description

This program checks whether a number is divisible by **3 or 4**.

### Concept Used

* `if-elif-else`
* `%` modulus operator
* Logical OR (`or`)
* Logical AND (`and`)

### Code

```python
num = eval(input("Enter the number: "))

if num % 3 == 0 or num % 4 == 0:
    print("Divisible")
elif num % 3 == 0 and num % 4 == 0:
    print("Divisible by both")
else:
    print("Not divisible by any one")
```

### ⚠️ Important Logic Note

In the original code, the `or` condition comes before the `and` condition:

```python
if num % 3 == 0 or num % 4 == 0:
```

Therefore, a number divisible by **both 3 and 4** will already enter the first condition.

If you specifically want to identify numbers divisible by both, check the `and` condition first:

```python
if num % 3 == 0 and num % 4 == 0:
    print("Divisible by both")
elif num % 3 == 0 or num % 4 == 0:
    print("Divisible by 3 or 4")
else:
    print("Not divisible by 3 or 4")
```

---

# 3️⃣ String Length Classification

### 📌 Description

This program determines whether a string contains one, two, three, or more than three characters.

### Code

```python
num = "12365"

if len(num) == 1:
    print("Single")
elif len(num) == 2:
    print("Double")
elif len(num) == 3:
    print("Triple")
else:
    print("Above 3")
```

### Example Output

```text
Above 3
```

### Concepts Covered

* Strings
* `len()`
* Conditional statements

---

# 4️⃣ String and Tuple Type Check

### 📌 Description

This program checks the data type of a variable.

* If the value is a string, it prints its length.
* If the value is a tuple, it prints the tuple in reverse order.
* Otherwise, it displays an invalid message.

### Code

```python
a = eval(input("Enter the character: "))

if isinstance(a, str):
    print(len(a))
elif isinstance(a, tuple):
    print(a[::-1])
else:
    print("Invalid")
```

### Concepts Covered

* `isinstance()`
* Strings
* Tuples
* String/tuple slicing
* `[::-1]`

### ⚠️ Note

Using `eval()` with user input is unsafe because it can execute arbitrary Python code. For beginner practice, it is better to use `input()` and explicitly process the required data type.

---

# 5️⃣ Age Category

### 📌 Description

This program categorizes a person based on their age.

| Age    | Category       |
| ------ | -------------- |
| 0–17   | Child          |
| 18–30  | Adult          |
| 31–60  | Men            |
| 61–100 | Senior Citizen |
| Other  | Invalid        |

### Code

```python
age = eval(input("Enter the age: "))

if age >= 0 and age <= 17:
    print("Child")
elif age >= 18 and age <= 30:
    print("Adult")
elif age >= 31 and age <= 60:
    print("Men")
elif age >= 61 and age <= 100:
    print("Senior Citizen")
else:
    print("Invalid")
```

### Concepts Covered

* Range checking
* Comparison operators
* Logical `and`
* `if-elif-else`

---

# 6️⃣ Find the Smallest of Three Numbers

### 📌 Description

This program accepts three numbers and determines which one is the smallest.

### Code

```python
a = eval(input("Enter the number: "))
b = eval(input("Enter the number: "))
c = eval(input("Enter the number: "))

if a < b and a < c:
    print("a is Smaller")
elif b < a and b < c:
    print("b is Smaller")
else:
    print("c is Smaller")
```

### Concepts Covered

* Comparison operators
* Logical `and`
* Multiple conditions
* Finding minimum values

### ⚠️ Note

The above logic assumes the numbers are different. If two or more numbers are equal, the result may not accurately describe the smallest value.

A more robust approach would be:

```python
print("Smallest:", min(a, b, c))
```

---

# 7️⃣ Student Marks and Grade Classification

### 📌 Description

This program accepts marks for five subjects, calculates the total and average, and determines the student's classification.

### Code

```python
m = eval(input("Enter the marks: "))
e = eval(input("Enter the marks: "))
h = eval(input("Enter the marks: "))
ma = eval(input("Enter the marks: "))
s = eval(input("Enter the marks: "))

total = m + e + h + ma + s
avg = total / 5

if avg >= 90 and avg <= 100:
    print("Distinction", avg)
elif avg >= 75 and avg <= 89:
    print("First Class", avg)
elif avg >= 60 and avg <= 74:
    print("Second Class", avg)
elif avg >= 50 and avg <= 59:
    print("Third Class", avg)
else:
    print("Fail", avg)
```

### Classification

|  Average | Result       |
| -------: | ------------ |
|   90–100 | Distinction  |
|    75–89 | First Class  |
|    60–74 | Second Class |
|    50–59 | Third Class  |
| Below 50 | Fail         |

### ⚠️ Important Correction

The original code uses:

```python
if avg >= 50 and avg <= 59:
```

after the previous `elif` conditions.

It should be:

```python
elif avg >= 50 and avg <= 59:
```

Otherwise, the `else` is connected only to the last `if`, which can produce an incorrect **Fail** message.

---

# 8️⃣ Username and Password Validation

### 📌 Description

This program checks a username and password against predefined credentials.

### Code

```python
username1 = input("Enter Username: ")
username = "Pranay"

password1 = input("Enter the Password: ")
password = "12345"

if username1 == username and password1 == password:
    print("Login Successful")
elif username1 == username and password1 != password:
    print("Incorrect Password")
elif username1 != username and password1 != password:
    print("User not found")
else:
    print("Invalid Both")
```

### Possible Results

```text
Login Successful
```

```text
Incorrect Password
```

```text
User not found
```

### Concepts Covered

* String comparison
* Logical `and`
* User input
* Authentication logic

### 🔐 Security Note

This is only an educational example. Real applications should **never hard-code passwords** or store passwords as plain text.

---

# 9️⃣ Positive/Negative and Even/Odd Classification

### 📌 Description

This program determines whether a number is:

* Positive Even
* Positive Odd
* Negative Even
* Negative Odd
* Zero

### Code

```python
x = eval(input("Enter the number: "))

if x >= 0 and x % 2 == 0:
    print("Positive Even")
elif x > 0 and x % 2 != 0:
    print("Positive Odd")
elif x < 0 and x % 2 == 0:
    print("Negative Even")
elif x < 0 and x % 2 != 0:
    print("Negative Odd")
else:
    print("Zero")
```

### Example

For:

```text
8
```

Output:

```text
Positive Even
```

For:

```text
-7
```

Output:

```text
Negative Odd
```

### Concepts Covered

* Positive/negative number checking
* Even/odd checking
* Modulus operator
* Multiple conditions
* Logical operators

---

# 🔟 Battery and Money Decision System

### 📌 Description

This program makes a decision based on two conditions:

* Available money
* Battery percentage

### Code

```python
Battery = eval(input("Enter the battery percentage: "))
Money = eval(input("Enter the money: "))

if Money >= 1000 and Battery >= 80:
    print("Go on a Trip")
elif Money >= 500 and Battery >= 50:
    print("Watch a Movie")
elif Money >= 200 and Battery >= 20:
    print("Go to a Café")
else:
    print("Stay Home and Study Python 🐍")
```

### Decision Table

|     Money | Battery | Decision        |
| --------: | ------: | --------------- |
|    ≥ 1000 |   ≥ 80% | Go on a Trip    |
|     ≥ 500 |   ≥ 50% | Watch a Movie   |
|     ≥ 200 |   ≥ 20% | Go to a Café    |
| Otherwise |       — | Study Python 🐍 |

### Concepts Covered

* Multiple conditions
* Logical `and`
* Comparison operators
* Decision-making

---

# 🧠 Python Concepts Practiced

This collection provides practice with several fundamental Python concepts.

### Conditional Statements

```python
if condition:
    ...
elif condition:
    ...
else:
    ...
```

### Comparison Operators

```text
>
<
>=
<=
==
!=
```

### Logical Operators

```python
and
or
```

### Modulus Operator

```python
num % 2
```

Used for checking even and odd numbers.

### String Length

```python
len(value)
```

### Type Checking

```python
isinstance(value, str)
```

### Slicing

```python
value[::-1]
```

---

# ▶️ How to Run

Make sure Python 3 is installed.

Check the version:

```bash
python --version
```

Run any program using:

```bash
python filename.py
```

For example:

```bash
python 09_number_classification.py
```

---

# 📚 Learning Objectives

By completing these programs, you can practice:

* Writing `if-else` statements
* Using `if-elif-else`
* Combining conditions using `and` and `or`
* Comparing numbers and strings
* Working with user input
* Performing basic calculations
* Classifying data based on conditions
* Implementing simple real-world decision logic
* Identifying and correcting logical errors

---

# 🔮 Future Improvements

These programs can be further improved by:

* Replacing `eval()` with safer input handling
* Adding exception handling
* Creating reusable functions
* Adding loops for repeated execution
* Creating menu-driven programs
* Building GUI versions using Tkinter
* Creating web versions using Flask
* Adding automated test cases

---

# ⚠️ Important Python Practice Notes

### Avoid `eval(input())`

Several programs use:

```python
eval(input())
```

For learning basic syntax, it may appear convenient, but it is **not recommended for real applications** because `eval()` can execute arbitrary Python expressions.

Prefer:

```python
num = int(input("Enter the number: "))
```

or:

```python
num = float(input("Enter the number: "))
```

depending on the expected input.

---

# 👨‍💻 Author

**Pranay Jadhao**

Electronics & Telecommunication Engineer

Aspiring Software Engineer | Python | Java | JavaScript | SQL | Flask | Firebase

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and improve these programs for educational and learning purposes.

---

⭐ **If you found this collection useful, consider starring the repository!**
