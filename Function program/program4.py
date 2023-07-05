#nth term of fibonacci series
def fibonacii(n):
    if(n==0)or(n==1):
        return 1
    else:
        return n+fibonacii(n-1)

term=int(input("enter the term:"))
x=fibonacii(term)
print(x)
