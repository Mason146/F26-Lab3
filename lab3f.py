# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 10/2/26
# Purpose: 2D List

# Usage: ./lab3f.py

# Follow the specific instructions given in the README.md file
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

element = matrix[1][2] # Output: 6
# Print element 5
print(matrix[1][1])
# Print element 2
print(matrix[0][1])
# Print element 9
print(matrix[2][2])
# Print each individual list
for row in matrix:
    print(row)