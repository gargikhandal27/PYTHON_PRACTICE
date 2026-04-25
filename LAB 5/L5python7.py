n = int(input("Enter a number : "))
if n >1:
    for i in range(2,(n//2)+1):
        if n%i==0:
            print("NOT A PRIME NUMBER")

elif n<=1:
    print("Invalid")
else:
    print("IT IS A PRIME NUMBER ")