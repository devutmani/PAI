tuple = ()

size = int(input("Enter size: "))

if not (size == 1):
    for i in range(size):
        ele = int(input("Enter element: "))
        tuple2 = (ele,)
        tuple += tuple2

    min = tuple[0]+tuple[1]
    currentTuple = (tuple[0], tuple[1])

    for i in range(0, len(tuple2)):
        for j in range(i+1, len(tuple)):
            if (tuple[i]+tuple[j]) < min:
                min = tuple[i]+tuple[j]
                currentTuple = ()
                currentTuple = (tuple[i], tuple[j])

    print("\nPair with sum closest to zero:", currentTuple)
    print("Nearest to zero:", min)
else:
    print("Not Valid")