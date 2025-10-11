password = input("Enter password: ")

alphChar = False
specialChar = False
passCount = 0

for i in password:
    passCount += 1

    if (i >= 'a' and i <= 'Z') or (i >= 'A' and i <= 'Z'):
        alphChar = True
    elif not ((i >= 'a' and i <= 'Z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9')):
        specialChar = True

if passCount >= 8 and alphChar and specialChar:
    print("Valid")
else:
    print("Not Valid")