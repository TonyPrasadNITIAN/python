num=input("enter the number to check prime ")
count=0
if num >1:
    for i in range (1,num-1):
        if (num%i)==0:
         count =count+1
    if count>1:
     print("it is not a prime number ",num)
    else:
     print("it is  prime number ",num)
