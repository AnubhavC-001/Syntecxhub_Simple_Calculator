# cli_calculator.py

from calculator_logic import add, subtract, multiply, divide

def main():
    while True:
        print("\n===== Simple Calculator =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Clear")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "6":
            print("Exiting... 👋")
            break

        if choice == "5":
            print("Calculator cleared.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except:
            print("Invalid input! Please enter numbers.")
            continue

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()