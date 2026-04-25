l=[]
s=[]
n = input("Enter string: ")
for i in n:
    l.append(i)
for j in range (1,len(l)+1):
    s.append(l[len(l)-j])
if l==s:
    print("Palindrome")
else:
    print("Not")
