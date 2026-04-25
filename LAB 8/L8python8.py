a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
l = [a, b, c]
print("Sum: ",l[0]+l[1]+l[2])
print("Product: ",l[0]*l[1]*l[2])
if l[0]<l[1] and l[0]<l[2]:
    print(l[0])
elif l[1]<l[0] and l[1]<l[2]:
    print(l[1])
elif l[2]<l[0] and l[2]<l[1]:
    print(l[2])
