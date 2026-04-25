x = int(input("Enter integer : "))
if x<0:
    print("invalid")
i=0
while x>0:
    b = x%10
    i = i + b
    x = x//10
print(i)