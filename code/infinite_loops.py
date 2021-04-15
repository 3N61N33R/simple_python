"""loop that keeps executing and never stops"""

while x % 2 == 0:
    x = x / 2

# break the loop by inserting the while loop inside an if statement

if x != 0:
    while x % 2 == 0:
        x = x / 2

# add a condition
while x != 0 and x % 2 == 0:
    x = x / 2

# fix this
def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)

# requires external signal to stop
while True:
    do_something_cool()
    if user_requested_to_stop():
        break
