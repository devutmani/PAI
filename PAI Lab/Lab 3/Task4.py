list1 = input("Enter element in list 1: ").split()
list2 = input("Enter element in list 2: ").split()

isInt = input("\nAre list 1's inputs are integers? (y/n): ")
if isInt.lower() == 'y':
    for i in range(len(list1)):
        list1[i] = int(list1[i])

isInt = input("Are list 2's inputs are integers? (y/n): ")
if isInt.lower() == 'y':
    for i in range(len(list2)):
        list2[i] = int(list2[i])

dic = {list1[i] : list2[i] for i in range(len(list1))}
print(dic)

string = ""

for key, value in dic.items():
    string += f"{key} : {value}\n"

with open("demo.txt", "w") as file:
    file.write(string)