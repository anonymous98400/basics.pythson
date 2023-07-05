""" A program should read “n” positive integers from the user and
append it to the list, and if the list contains prime numbers return “True” and number of prime numbers, else “False”. """

def is_prime(n):
    
    for i in range(2,n):
        if n % i == 0:
            return False
        

n = int(input("Enter the number of integers: "))
numbers = []
print(n)
for i in range(n):
    num = int(input("Enter a positive integer: "))
    numbers.append(num)
print(numbers)
prime_numbers = [num for num in numbers if (is_prime(num) != False)]
num_primes = len(prime_numbers)
print("Number of prime numbers:", num_primes)
