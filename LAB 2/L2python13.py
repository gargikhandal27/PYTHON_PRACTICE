x = int(input("Enter salary : "))
if x<300000:
    print("0")
elif 300000<= x <=1000000:
    print((10*x/100))
elif 1000000< x <= 2500000:
    print((20*x/100))
elif x>= 2500000:
    print((30*x)/100)
    