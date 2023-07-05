""" Write a program that generates a set of squares of numbers in the range(1-30) and another list generates numbers that are divisible by 3 in the range(1-30).
Generate a newset from a square set, which should not contain the numbers that are divisible by 3. """

squares = {num**2 for num in range(1, 31)}


divisible_by_3 = [num for num in range(1, 31) if num % 3 == 0]


new_set = {num for num in squares if num not in divisible_by_3}


print("Squares Set:", squares)
print("Divisible by 3 List:", divisible_by_3)
print("New Set:", new_set)
