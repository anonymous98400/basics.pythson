""" Write a python program to remove even numbers from the given list.
Sample Input: [5,6,2,8,9,12,66] Sample Output [5,9] """

num=[5,6,2,8,9,12,66]
print(num)
list=[]
for i in num:
    if i%2==0:
        continue
    list.append(i)
print(list)
