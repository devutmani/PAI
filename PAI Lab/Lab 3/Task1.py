def calculateArea(length, width):
    return length*width

length = float(input("\nEnter length: "))
width = float(input("Enter width: "))

print(f"\nArea: {calculateArea(length, width)}")