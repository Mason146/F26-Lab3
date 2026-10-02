# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 10/2/26
# Purpose: Modify a list using a loop
# Usage: ./lab3e.py

# Follow the specific instructions given in the README.md file
# Create list with students
students = ["Ama", "Elina", "Maija", "Daniel", "Ibrahim"]
# Change element at index 1 and update element to "Maggy"
students[1] = "Maggy"
# Use for loop and iterate over this list and print each element on a separate line
for student in students:
    print(student)