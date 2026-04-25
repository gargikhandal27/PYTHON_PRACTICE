n = int(input("Enter a number : "))
e = float(input("Enter a number : "))
i = 1
sum1 = 0
sum2 = 0
while 0<i<=n:
    sum1 = sum1 + (1/2)**i
    sum2 = sum2 + (1/2)**(i-1)
    if sum1 - sum2 < e:
        #print(sum1)
        break
    i = i + 1

print(sum1)       