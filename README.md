# Menu-Driven Calculator

**Name:** Aditya Singh
**ERP ID:** RU-26-02606
**PS No.:** 7
**University:** Rungta International Skills University – School of Computer Science and Engineering

---

## Project Overview

Menu-Driven Calculator is a console-based Python program that repeatedly shows a menu of arithmetic operations. The user picks an operation, enters two numbers and the program displays the result rounded to 2 decimal places. It handles errors such as division by zero, non-numeric input and invalid menu choices without crashing, and keeps running until the user chooses Exit.

## Objectives

- Build a loop-driven menu that runs until the user selects Exit.
- Write a separate function for each operation (add, subtract, multiply, divide, power, modulus).
- Handle division by zero and non-numeric input using `try-except`.
- Validate the menu choice and display every result rounded to 2 decimal places.

## Features

- Menu with 7 options:

```
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Modulus
7. Exit
```

- Works with whole numbers, decimals and negative numbers
- Every result shown with 2 decimal places, e.g. `Result: 12 + 8 = 20.00`
- Error handling:
  - Division / modulus by zero → `Error: Division by zero is not allowed.`
  - Text instead of a number → `Error: Invalid number. Enter numeric values only.`
  - Menu choice outside 1–7 → `Invalid choice. Select 1 to 7.`
  - Very large power results → `Error: Result is too large to calculate.`
- Program never crashes on wrong input; it shows the menu again

## Requirements

- Python 3.8 or above
- No external libraries (only built-in Python)

## Project Structure

```
MenuDrivenCalculator/
├── one.py                     # complete project code
├── README.md
├── test_cases.txt             # inputs and expected output of all test cases
├── Test_Case_Screenshots.pdf  # screenshots of all test cases
└── screenshots/
    ├── test1_output.png
    ├── test2_output.png
    ├── test3_output.png
    └── test4_output.png
```

## How to Run

1. Open a terminal / command prompt in the project folder.
2. Run the program:

```
python one.py
```

(On Windows you can also use `py one.py`.)

3. Enter a menu choice (1–7).
4. For options 1–6, enter the first and second number when asked.
5. The result is shown and the menu appears again. Enter `7` to exit.

## Input Details

| Input | Description |
|-------|-------------|
| Menu choice | A number from 1 to 7 |
| First number | Any integer or decimal (e.g. 12, -3, 9.5) |
| Second number | Any integer or decimal |

## Output Details

- Result in the form `Result: <a> <symbol> <b> = <answer>` with the answer rounded to 2 decimal places
- Symbols used: `+` add, `-` subtract, `*` multiply, `/` divide, `^` power, `%` modulus
- An error message for invalid input, after which the menu is shown again
- `Thank you for using the calculator. Exiting...` on option 7

## Test Cases

| # | Type | Input | Expected Output | Result |
|---|------|-------|-----------------|--------|
| 1 | Normal | Option 1 (Add): 12 and 8 | 12 + 8 = 20.00 | Pass |
| 2 | Boundary / Minimum | Option 4 (Divide): 0 and 5 (zero numerator) | 0 / 5 = 0.00 | Pass |
| 3 | Invalid | (a) Option 4: 10 and 0<br>(b) Option 3: abc and 4<br>(c) Menu choice 9 | (a) Error: Division by zero is not allowed.<br>(b) Invalid number. Enter numeric values only.<br>(c) Invalid choice. Select 1 to 7. | Pass |
| 4 | Different valid scenario | (a) Option 5: 2 and 10<br>(b) Option 6: 17 and 5<br>(c) Option 2: 5 and 9.5<br>(d) Option 7 | (a) 2 ^ 10 = 1024.00<br>(b) 17 % 5 = 2.00<br>(c) 5 - 9.5 = -4.50<br>(d) Thank you for using the calculator. Exiting... | Pass |

Screenshots of input and output for every test case are in `Test_Case_Screenshots.pdf` and the `screenshots/` folder.

## Concepts Used

- Functions (one function per operation)
- `while` loop for the menu, `break` and `continue`
- Arithmetic operators: `+ - * / ** %`
- Exception handling: `try-except` for `ValueError`, `ZeroDivisionError`, `OverflowError`
- Dictionary to map menu choices to functions
- String formatting to 2 decimal places (`{:.2f}`)

## Conclusion

The calculator performs all six arithmetic operations correctly, keeps running until the user exits, and handles invalid input safely. All four given test cases produce the expected output.
Mentored by: Mr. Satyaprakash Sethy

GitHub: @SATYAPRAKASHSETHY

ike thigion Mentor/ Technical Guide"
