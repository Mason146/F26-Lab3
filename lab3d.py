# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 10/2/26
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3d.py

# Follow the specific instructions given in the README.md file
# Create mylist that contains first 6 natural numbers
mylist = [1, 2, 3, 4, 5, 6]
# Use append method and add 7 to list
mylist.append(7)
# Use insert method and insert element 0 at index 0
mylist.insert(0, 0)
# Use the pop method to remove the element from index 2
mylist.pop(2)
# Print mylist
print(mylist)
# Add another statement in the script to find the index of the element 6 and print 'The element 6 is present at the index ---'
# Use .index() to return index value
index = mylist.index(6)
print("The element 6 is present at the index", index)