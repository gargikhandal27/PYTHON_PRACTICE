n = int(input("Enter a number : "))
a = 0
b = 0
c = 0
d = 0
e = 0
while n!=-1:
    if 1<=n<=2:
        a+=1
    elif 3<=n<=4:
        b+=1
    elif 5<=n<=6:
        c+=1
    elif 7<=n<=8:
        d+=1
    elif 9<=n<=10:
        e+=1
    else:
        print("Invalid Input")
    n = int(input("Enter a number : "))
print("1-2:","#"*a,(a*100)/(a+b+c+d+e))
print("3-4:","#"*b,(b*100)/(a+b+c+d+e))
print("5-6:","#"*c,(c*100)/(a+b+c+d+e))
print("7-8:","#"*d,(d*100)/(a+b+c+d+e))
print("8-9:","#"*e,(e*100)/(a+b+c+d+e))     