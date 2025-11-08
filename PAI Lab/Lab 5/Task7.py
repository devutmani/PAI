def fixMistakeInFile():
    try:
        filePath = "replacement_needed.txt"
        with open(filePath, 'r', encoding='utf-8') as file:
            content = file.read()

        print("Original content:", content)

        letterCount = {}
        for char in content:
            if char.isalpha():  
                if char in letterCount:
                    letterCount[char] += 1
                else:
                    letterCount[char] = 1

        minCount = None
        wrongLetter = None
        for letter in letterCount:
            if minCount is None or letterCount[letter] < minCount:
                minCount = letterCount[letter]
                wrongLetter = letter

        print(f"Detected unusual letter: '{wrongLetter}' (appears {minCount} time(s))")

        newLetter = input(f"Enter the correct letter to replace '{wrongLetter}': ")

        if len(newLetter) != 1:
            print("Error: Please enter only one character.")
            return

        correctedContent = ""
        for char in content:
            if char == wrongLetter:
                correctedContent += newLetter
            else:
                correctedContent += char

        with open(filePath, 'w', encoding='utf-8') as file:
            file.write(correctedContent)

        print("\nCorrected content saved successfully:")
        print(correctedContent)

    except FileNotFoundError:
        print(f"Error: The file '{filePath}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{filePath}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

fixMistakeInFile()