#calculates the power of the numbers 
def power(a,b):
    x=a**b
    return x
base=int(input("enter the base:"))
expo=int(input("enter the power:"))
result=power(base,expo)
print(result)
