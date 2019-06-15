# Ask the user for a number and then print
# the area of a circle with that number as the radius.

from math import pi
r=input("What is a number?")
print(pi*int(r)**2)

# Write a program that forms and prints a new string by exchanging
# the first and last characters in the string "mystery".
# V-1

last=(len('mystery')-1)
print ('mystery'[last]+'mystery'[1:last]+'mystery'[0])

# V-2

import math
print('mystery'[-1] + \
      'mystery'[1:math.floor(len('mystery')/2)] + \
      'mystery'[math.floor(len('mystery')/2):6] + \
                                              'mystery'[0])

# Ask the user for an input string of length at least two
# and print the string swapping out the first and second parts of it
# where second half is in upper case and the first half is in lower case.

from math import floor
name=input("Name a string with at least two characters")
mid=(floor(len(name)/2))
first_part = name[0:mid]
second_part = name[mid:]
print(second_part.lower()+first_part.upper())