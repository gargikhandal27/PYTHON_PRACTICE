x = int(input("Enter a number : "))
a = x
b = 0
while a>0:
    r = a % 10
    b = (b*10)+r
    a = a // 10
if x==b:
    print("It is pelindrome")
else:
    print("It is not pelidrome")