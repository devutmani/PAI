def employee(name, salary = 10_000):
    salary = salary-(2/100)*salary
    print(f"\nName: {name}\nSalary: {salary}")

name = input("\nEnter name: ")
salary = float(input("Enter salary: "))

employee(name, salary)