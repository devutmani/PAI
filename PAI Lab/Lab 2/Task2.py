matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]

print("\nMatrix 1:\n")
for row in matrix1:
    print(row)

print("\nMatrix 2:\n")
for row in matrix2:
    print(row)

matrix3 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matrix3[i][j] = matrix1[i][j]+matrix2[i][j]

print("\nSum Matrix:\n")
for row in matrix3:
    print(row)

matrix3 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for i in range(3):
    for j in range(3):
        for k in range(3):
            matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

print("\nMultiplication Matrix:\n")
for row in matrix3:
    print(row)