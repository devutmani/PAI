def isVowel(userInput):
    userInput = str(userInput).lower()
    if userInput[len(userInput)-1] == "a" or userInput[len(userInput)-1] == "e" or userInput[len(userInput)-1] == "i" or userInput[len(userInput)-1] == "o" or userInput[len(userInput)-1] == "u":
        return True
    else:
        return False

userInput = input("Enter input: ")
if isVowel(userInput):
    print(f"\n{userInput}'s last letter is a vowel.")
else:
    print(f"\n{userInput}'s last letter is a consonant.")