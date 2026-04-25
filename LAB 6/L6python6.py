n=int(input("Enter the number of terms : "))
nums=[]
a=1
for i in range(n):
    x=int(input("Enter the number : "))
    nums.append(x)
    

minimum=min(nums) 

for i in range(minimum,0,-1):

    is_a=True
    for j in nums:
        if i%j!=0:
            is_a=False
            break 
        if is_a:
            a=i
print("HCF : ", a)