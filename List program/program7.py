 #Write a python program that removes duplicates from the given list and generate the new list without duplicates.

n=int(input("Enter the number of integers to be taken"))
list=[]
list1=[]
print("Enter the numbers")
for i in range(n):
    num=int(input())
    list.append(num)
print(list)   
for j in list:
    if j not in (list1):
        list1.append(j)
print(list1) 
