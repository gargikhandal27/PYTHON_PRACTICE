'''x = int(input("Enter a number : "))
i=1
while i<=10:
    print("3 *",i,"=",x*i)
    i+=1'''
'''nums = [1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100]
idx = 0
while idx<len(nums):
    print(nums[idx])
    idx+=1'''
'''tup = (1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 , 36 )
n = 36
i = 0
while i<len(tup):
    if tup[i]==n:
        print(i)
    else: 
        print("FINDING")
    i+=1'''
#for loop 
'''num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in num:
    if i==23:
        break
    print(i)
else:
    print("end")'''
'''num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
for i in num:
    if i==49:
        print(num.index(i))
    '''
'''for i in range (1, 101, 1):
    if i%2==0:
        print(i)'''
'''for i in range (1, 101, 1):
    print(i)'''
'''for i in range (100, 0 , -1):
    print(i)'''
'''n = int(input("Enter a number : "))
for i in range (1, 11, 1):
    print(n,"*",i,"=",n*i)'''
#PRACTICE QUESTION
'''N = int(input("Enter a number : "))
i = 0
sum = 0
while i<=N:
    sum+=i
    i+=1
print(sum)'''
'''n = int(input("Enter a number : "))
fact = 1
for i in range (1, n):   
    fact = fact*i
    
print(fact)'''
#1
'''n = int(input("enter number : "))
for i in range (n):
    p=1
    for j in range (i,n):
        print(" ",end=" ")
    for j in range (i):
        print(p,end=" ")
        p+=1
    for j in range (i+1):
        print(p,end=" ")
        p+=1
    print()'''
#2
'''n = int(input("Enter a number : "))
for i in range (n):
    p=1
    for j in range (n):
        print(p,end=" ")
        p+=1
    print()'''
#3
'''n= int(input("Enter a number : "))
for i in range (n):
    p=1
    for j in range (i+1):
        print(p,end=" ")
        p+=1
    print()'''
#4
'''n = int(input("Enter a number : "))
for i in range (n):
    p=1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range (i+1):
        print(p,end=" ")
        p+=1
    print()'''
#5
'''n = int(input("Enter a number : "))
for i in range (n):
    p=1
    for j in range(i,n):
        print(p,end=" ")
        p+=1
    print()
'''
#6
'''n= int(input("Enter a number : "))
for i in range (n):
    p=1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range (i+1):
        print(p,end=" ")
        p+=1
    for j in range (i):
        print(p,end=" ")
        p+=1
    print()'''
#7
'''n = int(input("enter a number : "))
for i in range(n):
    p=1
    for j in range(i):
        print(" ",end=" ")
    for j in range (i,n):
        print(p,end =" ")
        p+=1
    for j in range (i,n-1):
        print(p,end=" ")
        p+=1
    print()'''
#8  
'''n=int(input("enter the number:"))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        if i==n-1 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i+1):
        if i==j or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#9
'''n = int(input("Enter : "))
for i in range (n):
    for j in range (n):
        if (j==0 and j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#10
'''n = int(input("Enter : "))
for i in range (n):
    for j in range (n):
        if j==n//2 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
    #11
'''n = int(input("Enter : "))
for i in range (n):
    for j in range (n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  '''
#12
'''n = int(input("Enter : "))
for i in range (n):
    for j in range (n):
        if j==0 or j==n-1:
            print("*",end=" ")
        elif i==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#13
'''n= int(input("Enter :"))
for i in range (n):
    for j in range (i+1):
        if j==0 or i==j or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#14
'''n = int(input("Enter : "))
for i in range (n):
    for j in range ( n):
        if i==0 or i==j or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
        