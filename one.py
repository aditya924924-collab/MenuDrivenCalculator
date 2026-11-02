# Menu-Driven Calculator
# Name    : Aditya Singh
# ERP ID  : RU-26-02606
# PS No.  : 7
# Rungta International Skills University
#
# A console calculator that keeps showing a menu of arithmetic
# operations, takes two numbers, shows the result rounded to
# 2 decimal places and handles errors until the user exits.


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b          # raises ZeroDivisionError when b is 0


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b          # raises ZeroDivisionError when b is 0


# menu number -> (name, function, symbol)
operations = {
    "1": ("Add", add, "+"),
    "2": ("Subtract", subtract, "-"),
    "3": ("Multiply", multiply, "*"),
    "4": ("Divide", divide, "/"),
    "5": ("Power", power, "^"),
    "6": ("Modulus", modulus, "%"),
}


def show_menu():
    print("\n========== CALCULATOR MENU ==========")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")
    print("=====================================")


def fmt(num):
    # shows 12.0 as 12 and 9.5 as 9.5 in the expression
    return "{:g}".format(num)


def get_numbers():
    first = input("Enter first number : ").strip()
    second = input("Enter second number: ").strip()
    return float(first), float(second)   # raises ValueError for text like 'abc'


def main():
    print("Welcome to the Menu-Driven Calculator")

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("Thank you for using the calculator. Exiting...")
            break

        if choice not in operations:
            print("Invalid choice. Select 1 to 7.")
            continue

        name, func, symbol = operations[choice]
        print("--", name, "--")

        try:
            a, b = get_numbers()
            result = func(a, b)
            print("Result: {} {} {} = {:.2f}".format(fmt(a), symbol, fmt(b), result))
        except ValueError:
            print("Error: Invalid number. Enter numeric values only.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except OverflowError:
            print("Error: Result is too large to calculate.")


if __name__ == "__main__":
    main()
