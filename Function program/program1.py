def perfect_square(n):
    for i in range(1,100000):
        if(i*i==n):
           print(n,"is a square of ",i)
           global a
           a=a+1
a=0        
num=int(input("enter a number:"))
perfect_square(num)
if(a!=1):
    print("not a square")
