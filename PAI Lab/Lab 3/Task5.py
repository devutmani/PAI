def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
string = input("\nEnter string: ")
if isPalindrome(string):
    print(f"\n{string} is a palindrome.")
else:
    print(f"\n{string} is not a palindrome.")