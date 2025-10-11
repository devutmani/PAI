studentsList = [("Dev Kumar", 99), ("Gotam Lal", 67), ("Vikash", 34), ("Arav", 78), ("Fateh Singh", 56), 
        ("Sahil Kumar", 89), ("Sheela", 78), ("Pawan Lal", 24), ("Sonu Sharma", 45)]

sortedList = sorted(studentsList, key = lambda x : x[1], reverse=True)

for i, student in enumerate(sortedList[:3], start=1):
    print(i, student)