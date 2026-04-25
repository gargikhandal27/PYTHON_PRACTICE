
#1.
'''x = input("Enter alphabet : ")
lst = ["a","e","i","o","u","A","E","I","O","U"]
i=0
while i<=(len(lst)-1):
    if x==lst[i]:
        print("Vowel")
    i+=1
else:
    print("Consonent")'''
#2.
'''x = 2.19 * 10**14
y = 4.68 * 10**14
diff = y-x
z = diff/x
print(round(z*100))'''
#3.
'''x = 1
print(x)
x_str = str(x)
print("my fav num is",x,".","x = ",x)
print(("my fav num is"+x_str+"."+"x="+x_str)*3) '''
#4.
'''a,b=2,3
print(a)
print(b)'''
#5.
'''a = int(input("Enter lower limit: "))
b = int(input("Enter upper limit: "))
i=a
while i<=b:
    if i%7==0:
        print(i)
    if i==200:
        break
    i+=1'''
'''x = '{0} {2} {1}'.format("Aaditya", "Boy", "is a")
print(x)'''
'''def avg(a,b,c):
    avg=(a+b+c)/3
    return avg
a = avg(1,2,3)
print(a)'''
'''def pro(a=2,b=1):
    pro=a*b
    print(pro)
    return pro
pro(2,5)'''
#FUNCTIONS
#1
'''acd= list(map(str, input().split()))
def lst(list):
    print(len(list))
print(acd)
lst(acd)'''
#2.
'''L = list(map(str, input().split()))
def lst(list):
    print(list)
lst(L)'''
#3.
'''a = int(input('Enter a number : '))
def fact(n):
    i=1
    f=1
    while i<=n:
        f=f*i
        i+=1
    print(f)
    return f
fact(a)'''
#4.
'''a = float(input("Enter USD :"))
def inr(n):
    m=84.75*n
    print(m)
    return m
inr(a)'''
#5.
'''n = int(input("Enter a number : "))
def eo(a):
    if a%2==0:
        print("Even")
    else:
        print("Odd")
eo(n)
'''
class Student:
    name =" abcd"
    
a =Student()
print(a.name)
