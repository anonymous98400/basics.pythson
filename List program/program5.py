""" Write a python program which reads “n” words from the user, store it in the list and 
display the length of each word and display the longest word in the list."""

num=int(input("Enter the number of words to be entered:"))
list=[]
for i in range(0,num):
    string=str(input())
    list.append(string)
print(list)
print("Length of each word is:")
for string in (list):
     length=len(string)
     print(string,":",length)
long=list[i]
for string in (list):
     if len(string)>len(long):
        long=string
print("The longest word is:",long)
