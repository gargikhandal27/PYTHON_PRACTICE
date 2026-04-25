x = float(input("Enter taxable income : "))
if x<=20000:
    print("Tax : ", (x*2)/100)
elif x<=50000:
    y = x-20000
    z = (25 * y)/100
    print("Tax : ", 400 + z)
elif x>50000:
    a = x-50000
    b = (35 * a)/1000 
    print("Tax : ", 1150 + b)