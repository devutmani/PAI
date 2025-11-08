import json

def saveDictionaryToJson():
    try:
        dictionary = {}
        n = int(input("Enter number of entries: "))
        for i in range(n):
            name = input(f"Enter name of person {i+1}: ")
            age = int(input(f"Enter age of {name}: "))
            dictionary[name] = age

        filePath = input("Enter the file path to save the JSON: ")
        with open(filePath, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file)

        print(f"Dictionary saved successfully to '{filePath}'.")
        return filePath

    except ValueError:
        print("Error: Invalid input. Age must be a number.")
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filePath}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def loadJsonAndFindMaxAge(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            data = json.load(file)

        maxAge = None
        for age in data.values():
            if maxAge is None or age > maxAge:
                maxAge = age

        namesWithMaxAge = []
        for name, age in data.items():
            if age == maxAge:
                namesWithMaxAge.append(name)

        print(f"\nPerson(s) with maximum age ({maxAge}):")
        for name in namesWithMaxAge:
            print(name)

        ageCount = {}
        for age in data.values():
            if age in ageCount:
                ageCount[age] += 1
            else:
                ageCount[age] = 1

        print("\nAges that are shared by more than one person:")
        sharedAges = False
        for age, count in ageCount.items():
            if count > 1:
                print(f"Age {age} is shared by {count} people.")
                sharedAges = True

        if not sharedAges:
            print("No ages are shared by multiple people.")

    except FileNotFoundError:
        print(f"Error: The file '{filePath}' does not exist.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{filePath}'.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filePath}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


filePath = saveDictionaryToJson()
if filePath:
    loadJsonAndFindMaxAge(filePath)