x = int(input("Enter the number of rows: "))
a = (2 * x) - 2

for i in range(0, x):
    for j in range(0, a):
        print(end=" ")
    a = a - 1
    for j in range(0, i ,1):
        print("* ", end=' ')
    print()
    
    
   