number = int(input("\nEnter number: "))

print(f"\nFloat typed: {float(number)}")
print(f"String typed: {str(number)}")
print(f"Complex typed: {complex(number)}")

if (number // 2) * 2 == number:
    print(f"\n{number} is divisble by 2")
else:
    print(f"\n{number} is not divisble by 2")