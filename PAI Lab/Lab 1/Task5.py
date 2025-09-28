specialChar = "@#%&*"
name = input("\nEnter name: ")
birthYear = int(input("Enter birth year: "))
temp = birthYear

password = ""
for i in range(3):
    if temp%2 == 0:
        password += name[i].upper()
    else:
        password += name[i].lower()
    temp //= 10

password += str(birthYear%100)
password += specialChar[ord(name[0])%5]

print(f"\nPassword: {password}")