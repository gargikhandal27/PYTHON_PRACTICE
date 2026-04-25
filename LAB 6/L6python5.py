n=int(input("Enter the number of terms : "))
nums=[]
i=1
while i<=n:
    x=int(input("Enter the number : "))
    nums.append(x)
    i+=1
j=1
a=nums[0]
while j<len(nums):
    if a>nums[j]:
        greater=a
    else:
        greater=nums[j]
    while True:
        if greater%a==0 and greater%nums[j]==0:
            a=greater
            break
        else:
            greater+=1
    j+=1
print("LCM : ",a)
        