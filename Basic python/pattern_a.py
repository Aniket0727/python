# Practical No.5
# pattern - a
#   *
#   **
#   ***
#   ****

n = 5
for i in range(0, n):
    for j in range(0, i):
        print("* ",end="")
    print()