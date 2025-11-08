def createDictionaryFromLists():
    try:
        list1Input = input("Enter elements of the first list separated by spaces: ")
        list2Input = input("Enter elements of the second list separated by spaces: ")

        list1 = list1Input.split()
        list2 = list2Input.split()

        if len(list1) != len(list2):
            print("Error: Both lists must have the same number of elements.")
            return

        resultDict = {}
        for i in range(len(list1)):
            resultDict[list1[i]] = list2[i]

        filePath = input("Enter the file path to store the dictionary: ")
        with open(filePath, 'w', encoding='utf-8') as file:
            file.write(str(resultDict))

        print(f"Dictionary successfully saved to '{filePath}'")
        
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filePath}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

createDictionaryFromLists()