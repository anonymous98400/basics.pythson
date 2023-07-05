""" Write a program that generate a set of number that are prime numbers (1-50) and
another set of numbers divisible by 5 (1-50),then apply union, intersection, difference and symmetric difference on the resultant sets """


def is_prime(n):
    for i in range(2,n):
        if(n%i == 0):
            return False


prime_numbers = {num for num in range(1, 51) if (is_prime(num) != False)}


divisible_by_5 = {num for num in range(1, 51) if num % 5 == 0}


union = prime_numbers.union(divisible_by_5)
intersection = prime_numbers.intersection(divisible_by_5)
difference = prime_numbers.difference(divisible_by_5)
symmetric_difference = prime_numbers.symmetric_difference(divisible_by_5)


print("Prime Numbers:", prime_numbers)
print("Numbers Divisible by 5:", divisible_by_5)
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print("Symmetric Difference:", symmetric_difference)
