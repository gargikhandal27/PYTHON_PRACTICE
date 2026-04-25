x = float(input("Enter a number : "))
y = float(input("Enter another number : "))
N = float(input("Enter a number to divide : "))
i = x
while i<=y:
    if i%N==0:
        print(i)
        i=i+1