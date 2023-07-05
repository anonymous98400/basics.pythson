"""Write a python program that reads integers from the user and stores them in a list. Your program should continue reading values until the user enters 0.
Then it should display all of the values entered by the user (except for the 0) in ascending order (The list itself to be sorted)."""

print("Enter the numbers")
list=[]
while(True):
    num=int(input())
    print(num)
    if num==0:
        break
    list.append(num) 
print(list)  
list.sort()
print("The sorted list is:",list) 
