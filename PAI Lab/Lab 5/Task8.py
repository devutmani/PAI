def divideTwoNumbers():
    try:
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))

        result = num1 / num2
        print(f"The result of division is: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid integer numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

divideTwoNumbers()