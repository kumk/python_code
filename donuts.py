#Strings Exercise 1: Donuts
#
# Given an int count of a number of donuts, return a string of the form 'Number
# #of donuts: <count>', where <count> is the number passed in. However, if the
# #count is 10 or more, then use the word 'many' instead of the actual count.
# So #donuts(5) returns 'Number of donuts: 5' and donuts(23) returns
# 'Number of #donuts: many'

import sys

def numberofdonuts(count):
    if count < 10:
      print ("Number of donuts: ", count)    
    else:
      print ("Number of #donuts: many")
    


if __name__ == '__main__':
     numberofdonuts((int)(sys.argv[1]))
