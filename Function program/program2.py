#interest calculation
def interest_calculation(a,g,p):
    if(a>75):
        interest=p*(12/100)
        print("your interest",interest)
    elif(g=='F'):
        interest==p*(10/100)
        print("your interest",interest)
    else:
        interest==p*(9/100)
        print("your interest",interest)
name=str(input("enter your name "))
age=int(input("enter your age "))
gender=str(input("enter your gender "))
principal=int(input("enter the principal amount "))
interest_calculation(age,gender,principal)
