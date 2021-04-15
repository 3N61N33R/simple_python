"""while loops instruct your computer to continuosly execute your code based on the value of a condition
   pitfalls: ensure to initialize all variables
"""


def count_down(start_number):
    current = start_number
    while current > 0:
        print(current)
        current -= 1
    print("Zero!")


count_down(3)