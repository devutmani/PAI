def saveQuestionsToFile():
    try:
        sentence = input("Enter a sentence: ")

        if sentence.strip().endswith('?'):
            filePath = "questions.txt"
            with open(filePath, 'a', encoding='utf-8') as file:
                file.write(sentence + '\n')
            print(f"Question saved to '{filePath}'.")
        else:
            print("The sentence is not a question. It was not saved.")

    except PermissionError:
        print("Error: Permission denied to write to the file 'questions.txt'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

saveQuestionsToFile()