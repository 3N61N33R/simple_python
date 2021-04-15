# range
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
        print(n)
        n += 1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# Prime factors

def prime_factors(number):
    """ prints out the the prime factors of a number """
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
        # If it is, print it and divide the original number
        print(factor)
        number = number / factor
        else:
        # If it's not, increment the factor by one
        factor += 1
    return "Done"

prime_factors(100)
