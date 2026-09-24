from Addition import add
from Subtraction import subtract
from Multiplication import multiply
from Division import divide

from SquareRoot import square_root
from Power import power
from Factorial import factorial
from Logarithm import logarithm

from Trigonometry import sine, cosine, tangent


def display_menu():
    print("\n========== SCIENTIFIC CALCULATOR ==========")

    print("\nBasic Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    print("\nScientific Operations")
    print("5. Square Root")
    print("6. Power")
    print("7. Factorial")

    print("\nLogarithmic Operations")
    print("8. Logarithm")

    print("\nTrigonometry")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")

    print("\n0. Exit")
    print("============================================")


while True:

    display_menu()

    choice = input("\nEnter your choice: ")

    try:

        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", add(a, b))

        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", subtract(a, b))

        elif choice == "3":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", multiply(a, b))

        elif choice == "4":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", divide(a, b))

        elif choice == "5":
            number = float(input("Enter number: "))
            print("Result:", square_root(number))

        elif choice == "6":
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            print("Result:", power(base, exponent))

        elif choice == "7":
            number = int(input("Enter a non-negative integer: "))
            print("Result:", factorial(number))

        elif choice == "8":
            number = float(input("Enter number: "))
            base = float(input("Enter logarithm base (default 10): ") or "10")
            print("Result:", logarithm(number, base))

        elif choice == "9":
            angle = float(input("Enter angle in degrees: "))
            print("Result:", sine(angle))

        elif choice == "10":
            angle = float(input("Enter angle in degrees: "))
            print("Result:", cosine(angle))

        elif choice == "11":
            angle = float(input("Enter angle in degrees: "))
            print("Result:", tangent(angle))

        elif choice == "0":
            print("Calculator closed.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except Exception as e:
        print("Error:", e)