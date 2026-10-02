# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 10/2/26
# Purpose: Read input and multply by 10 and put in reverse order
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file
# Create empty list
numbers = []
# Create a while loop that ends when list size reaches 6
while len(numbers) < 6:
    # Add numbers to list using input
    num = int(input("Enter a number: "))
    # Multiply the numbers by 10
    numbers.append(num * 10)
# Reverse list
numbers.reverse()
# Print list
print(numbers)