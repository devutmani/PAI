def takeEmployeeBiodata():
    try:
        filePath = input("Enter the file path to save employee biodata: ")

        name = input("Enter employee name: ")
        cnic = input("Enter employee CNIC number: ")
        age = input("Enter employee age: ")
        salary = input("Enter employee salary: ")

        with open(filePath, 'w', encoding='utf-8') as file:
            file.write(f"Name: {name}\n")
            file.write(f"CNIC: {cnic}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Salary: {salary}\n")

        print(f"Biodata saved successfully in '{filePath}'.")

    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filePath}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def appendContactNumber():
    try:
        filePath = input("Enter the file path to append contact number: ")
        contactNumber = input("Enter employee contact number: ")

        with open(filePath, 'a', encoding='utf-8') as file:
            file.write(f"Contact Number: {contactNumber}\n")

        print("Contact number appended successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{filePath}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filePath}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def readEmployeeFile():
    try:
        filePath = input("Enter the file path to read employee data: ")

        with open(filePath, 'r', encoding='utf-8') as file:
            content = file.read()
            print("\n--- Employee Data ---")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filePath}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filePath}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

takeEmployeeBiodata()
appendContactNumber()
readEmployeeFile()