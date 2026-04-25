x=int(input("Enter the lower limit : "))
y=int(input("Enter the upper limit : "))
j=0

for i in range(x,y+1):
    if i>1:
        for n in range(2, int(i/2) + 1):
            if i%n==0:
                break
        else:
            j+=i

print("Sum of prime numbers :",j)