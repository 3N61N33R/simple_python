# Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.

def print_prime_factors(number):

# Start with two, which is the first prime

factor = \_\_\_

# Keep going until the factor is larger than the number

while factor <= number: # Check if factor is a divisor of number
if number % factor == **_: # If it is, print it and divide the original number
print(factor)
number = number / factor
else: # If it's not, increment the factor by one
_**
return "Done"

print_prime_factors(100)

# Should print 2,2,5,5

# DO NOT DELETE THIS COMMENT

# Fix infinite loop

def is_power_of_two(n):

# Check if the number can be divided by two without a remainder

while n % 2 == 0:
n = n / 2

# If after dividing by two the number is 1, it's a power of two

if n == 1:
return True
return False

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
sum = 0

# Return the sum of all divisors of n, not including n

return sum

print(sum_divisors(0))

# 0

print(sum_divisors(3)) # Should sum of 1

# 1

print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18

# 55

print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51

# 114
