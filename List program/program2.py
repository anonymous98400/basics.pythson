#The python program should read the list of 5 numbers, and generate the new list which contains the factorial of each number in the given list.


def factor(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factor(n-1)
num=[]
for i in range (5):
    num.append(int(input('List num: ')))
print(num)
# num=[2, 4, 8, 7, 5]
result =[]
for i in num:
    k =(factor(i))
    result.append(k)
print(result)
