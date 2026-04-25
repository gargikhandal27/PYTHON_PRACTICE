n = int(input("Enter a number : "))
i = 1
fact = 1
if n<0:
    print("Invalid")
while i<=n:
    fact = fact * i
    i+=1
print(fact) 