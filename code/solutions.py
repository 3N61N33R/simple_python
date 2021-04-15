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

# Sum of divisors
def sum_divisors(n):
    # Return the sum of all divisors of n, not including n
    sum = 0
    i = 1
    
    # res = n % i
    # if n % i == 0 and i < n:
    #   while n != 0:
    #     sum = sum + i
    #     print("<><><>", sum)
    #   i += 1

    x = 1
    while n != 0 and x < n :   
        if n % x == 0  :
        sum += x
        else:
        sum += 0
        x += 1    
    
    return sum

    # while res == 0 and i < n:
    #   sum += i
    #   i += 1
    # if n % i == 0:
    return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

def divisorSum( n ):
    sum = 0
    for i in range(1, n + 1):
        sum += int(n / i) * i
    return int(sum)
      
# Driver code
print( divisorSum(3))
print(divisorSum(36))

# PYTHON program to find sum of all
# divisors of a natural number
import math
     
# Function to calculate sum of all proper
# divisors num --> given natural number
def divSum(num) :
     
    # Final result of summation of divisors
    result = 0
     
    # find all divisors which divides 'num'
    i = 2
    print("<><><><>",num ** 0.5)

    while i <= (math.sqrt(num)) :
       
        # if 'i' is divisor of 'num'
        if (num % i == 0) :
       
            # if both divisors are same then
            # add it only once else add both
            if (i == (num / i)) :
                result = result + i;
            else :
                result = result +  (i + num/i);
        i = i + 1
         
    # Add 1 to the result as 1 is also
    # a divisor
    print(result + 1)
    return result + 1
    