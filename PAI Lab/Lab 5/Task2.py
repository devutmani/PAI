def replaceWordInFile(filePath, searchWord, replaceWord):
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            fileContent = file.read()
        
        modifiedContent = fileContent.replace(searchWord, replaceWord)
        
        with open(filePath, 'w', encoding='utf-8') as file:
            file.write(modifiedContent)
        
        print(f"All occurrences of '{searchWord}' have been replaced with '{replaceWord}'.")
        
    except FileNotFoundError:
        print(f"Error: The file '{filePath}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read/write the file '{filePath}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filePath = input("Enter the file path: ")
searchWord = input("Enter the word/phrase to search: ")
replaceWord = input("Enter the word/phrase to replace with: ")

replaceWordInFile(filePath, searchWord, replaceWord)