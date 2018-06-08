def lcm(x,y):
    if x > y:
        greater=x
    else:
        greater =y
    while(1):
        if((greater % x==0) and (greater % y==0)):
            lcm=greater
            break
        greater +=1
    return lcm
num1=input('enter the first number for LCM ')
num2=input('enter the second number for LCM ')
print'The LCM of of two number ',num1,'and',num2,'is',lcm(num1,num2)
