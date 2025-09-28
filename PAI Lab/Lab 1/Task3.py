number = input("\nEnter number: ")
print(f"\nOrignal number {number}")

if len(number) != 4 or not number.isdigit():
    print("\nPlease enter valid 4 digit number")
else:
    numberReversed = number[3]+number[2]+number[1]+number[0]

    for num in numberReversed:
        Num = (int(num)*7)%10
        encryptNum += str(Num)

    print(f"\nEncrypted Number: {encryptNum}")