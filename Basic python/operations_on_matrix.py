#  Practical No. 13
# Q.1. Write a Python program to create two matrices and 
    # perform addition, subtraction, multiplication and division operation on matrix.

M1 = [[1, 2],[4, 1]]
M2 = [[3, 2],[1, 2]]
print("matrix 1: ",M1)
print("matrix 2: ",M2)
print()
print("Addition of Two Matrix")

add=[[0, 0],[0, 0]]
for i in range(len(M1)):
    for j in range(len(M1[0])):
        add[i][j] = M1[i][j] + M2[i][j]
for num in add:
    print(num)

print()
print("Subtraction of Two Matrix")
M1 = [[1, 2],[4, 1]]
M2 = [[3, 2],[1, 2]]
add=[[0, 0],[0, 0]]
for i in range(len(M1)):
    for j in range(len(M1[0])):
        add[i][j] = M1[i][j] - M2[i][j]
for num in add:
    print(num)

print()
print("Multiplication of Two Matrix")
M1 = [[1, 2],[4, 1]]
M2 = [[3, 2],[1, 2]]
add=[[0, 0],[0, 0]]
for i in range(len(M1)):
    for j in range(len(M1[0])):
        add[i][j] = M1[i][j] * M2[i][j]
for num in add:
    print(num)

print()
print("Division of Two Matrix")
M1 = [[1, 2],[4, 1]]
M2 = [[3, 2],[1, 2]]
add=[[0, 0],[0, 0]]
for i in range(len(M1)):
    for j in range(len(M1[0])):
        add[i][j] = M1[i][j] / M2[i][j]
for num in add:
    print(num)