#Write a python program which reads “n” number of integers from the user and generates a separate list containing even and odd numbers.

n=int (input("Enter the number to be entered"))
number=[]
print("Enter the numbers to be added in list")
for i in range(n):
    num=int(input())
    number.append(num)
print(number)    
even=[]
odd=[]
for num in number:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd) 
