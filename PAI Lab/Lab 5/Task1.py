def countCharactersAndWords(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            textContent = file.read()
            characterCount = len(textContent)
            words = textContent.split()
            wordCount = len(words)
            print(f"Total characters: {characterCount}")
            print(f"Total words: {wordCount}")
    except FileNotFoundError:
        print(f"Error: The file '{filePath}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filePath}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filePath = input("Enter the file path: ")
countCharactersAndWords(filePath)