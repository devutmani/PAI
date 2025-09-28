list  = [1, 2, 3, 4, 5]

target = int(input("\nEnter target: "))

for i, element in enumerate(list):
    if target == element:
        print(f"\n{target} Found at index: {i}")
        break
else:
    print(f"{target} not Found!")