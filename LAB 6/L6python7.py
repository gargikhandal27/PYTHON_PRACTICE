import math
i=0
print('Degree\t','sin\t','cos')
while 0<=i<=360:
    print(i,'\t',end=' ')
    print(round(math.sin(i*math.pi/180),4),'\t',end='')
    print(round(math.cos(i*math.pi/180),4))
    i+=10