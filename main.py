# Ask the user for a number and then print the area of a circle with that number as the radius.

from math import pi
r=input("What is a number?")
print(pi*int(r)**2)

# Write a program that forms and prints a new string by exchanging the first and last characters in the string "mystery".
# V-1

last=(len('mystery')-1)
print ('mystery'[last]+'mystery'[1:last]+'mystery'[0])

# V-2

import math
print('mystery'[-1] + \
      'mystery'[1:math.floor(len('mystery')/2)] + \
      'mystery'[math.floor(len('mystery')/2):6] + \
                                              'mystery'[0])