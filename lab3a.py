# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 10/2/26
# Purpose: Generate a sequence of values
# Usage: ./lab3a.py

# Import random module to help generate random values
import random
# Create empty list numbers
numbers = []
# Create for loop to generate 20 random values between 0 and 99
for i in range(20):
    numbers.append(random.randint(0, 99))
# Print the original sequence
print("Random list")
print(numbers)
# Sort list with sort function
numbers.sort()
# Print the sorted sequence
print("Sorted list")
print(numbers)
