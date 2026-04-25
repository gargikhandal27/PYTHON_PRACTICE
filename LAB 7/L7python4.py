#a.
'''N=int(input("Enter the number of rows : "))
j=ord("A")
for i in range(1,N+1):
    print(" "*(N-i),end=" ")
    for k in range(1,i+1):
        print(chr(j+k-1),end="")
    print()'''
  #b.
'''N=int(input("Enter the number of rows : "))
a=ord("A")
print("A")
for i in range(1,t-1):
    print("A",end="")
    for j in range(1,i):
        print(" ",end="")
    print("B")
for k in range(1,t):
    print(chr(a+k-1),end="") ''' 
#c.
'''N=int(input("Enter the number of rows : "))
a=ord("A")
for i in range(1,t+1):
        print(" "*(t-i),end='')
        
        for j in range(a,a+2*i-1):
             print(chr(j), end='')
        print()'''
#d.
'''N=int(input("Enter number of rows : "))
print("*"*x,end="")
print()
for i in range (0,x-2):
    print("*",end="")
    print(" "*i,end="")
    print("*",end="")
    print(" "*(x-3-i),end="")
    print("*",end="")
    print()
print("*"*x,end="")
print()'''