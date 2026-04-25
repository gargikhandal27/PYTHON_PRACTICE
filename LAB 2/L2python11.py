x = int(input("Enter a number 1 : "))
y = int(input("Enter a number 2 : "))
z = int(input("Enter a number 3 : "))
if x>y and x>z:
    print(x)
elif x>y and z>x:
    print(z)
elif y>x and y>z:
    print(y)
elif y>x and z>y:
    print(z)