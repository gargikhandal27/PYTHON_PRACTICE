#A
'''n = int(input("Enter a number : "))
i = 1
sum = 0
while i<=n:
    sum = sum + (1/i)
    i = i+1
print(sum)'''
#B
'''n = int(input("Enter a number : "))
i = 1
fact = 1
sum = 0
while i<=n:
    fact = fact*i
    i = i+1
    sum = sum+(1/fact)
print(sum)'''
#C
'''n = int(input("Enter a number : "))
i = 1
sum = 0
while i<=n:
    sum = sum + (-1)**(i-1)*(1/i)**2
    i = i+1
print(sum)'''
#D
'''n = int(input("Enter a number : "))
x = int(input("Enter numerator : "))
i = 1
fact = 1
sum = 1
while i<=n:
        fact = fact*i
        sum = sum + x**i/(fact)
        i=i+1
print(sum)'''
#E
'''n = int(input("Enter a number : "))
x = int(input("Enter numerator : "))
i = 1
sum = 1
while i<=n:
    sum = sum + x**i/i
    i = i+1
print(sum)'''


    
    
    