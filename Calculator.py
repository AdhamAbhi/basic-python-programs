def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            # Get user input
            choice = input("Enter the number of the operation you'd like to perform (1/2/3/4): ")

            # Validate input
            if choice not in ('1', '2', '3', '4'):
                print("Invalid input. Please choose a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform operations
            if choice == '1':
                print(f"The result of addition: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"The result of subtraction: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"The result of multiplication: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Division by zero is not allowed.")
                else:
                    print(f"The result of division: {num1} / {num2} = {num1 / num2}")

            # Ask if the user wants to perform another operation
            next_calculation = input("Would you like to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter numeric values for the numbers.")

if __name__ == "__main__":
    calculator()
