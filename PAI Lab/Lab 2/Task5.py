students = {}

choice = True

print("\nBank Management System\n")
while choice:
    print("\n1. Add student name + marks in a dictionary\n2. Update marks\n3. Delete a student\n4. Find the topper\n5. Show Students and Their marks\n6. Exit")
    n = int(input("\nEnter choice: "))

    if n == 1:
        name = input("\nEnter student name: ")
        marks = int(input("Enter marks: "))

        students[name] = marks

    elif n == 2:
        name = input("\nEnter that student name: ")
        marks = int(input("Enter new marks: "))

        students[name] = marks

    elif n == 3:
        name = input("\nEnter that student name: ")
        students.pop(name, None)

    elif n == 4:
        max = 0
        for i in students.keys():
            if students[i] > max:
                max = students[i]
                name = i

        topper = {}
        topper[name] = max
        print(topper)

    elif n == 5:
        print(students)

    elif n == 6:
        choice = False

    else:
        print("\nInvalid Input!")