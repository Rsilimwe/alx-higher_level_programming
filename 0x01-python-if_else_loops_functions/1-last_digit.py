#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Print the original number
print("{}".format(number), end=" ")

# Calculate the last digit of the number
last_digit = abs(number) % 10

# Print the required output based on the last digit
print("is {:d} and is".format(last_digit), end=" ")

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
