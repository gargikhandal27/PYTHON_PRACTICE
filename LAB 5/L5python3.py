N = int(input("Enter a number : "))
c=0
while True :
    l=int(input("Enter a number : "))
    if l==-999:
        break
    elif l%N==0:
        c=c+1
print(c)