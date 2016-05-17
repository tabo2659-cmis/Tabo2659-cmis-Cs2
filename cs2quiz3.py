
#Section 1: Terminology
# 1) What is a recursive function?
#A recursive function is a function that calls itself until it meets the requirments of the base case where it stops.
#
#
# 2) What happens if there is no base case defined in a recursive function?
#It will recurse infinitly or about a 1000 times depending on the computer.
#
#
# 3) What is the first thing to consider when designing a recursive function?
# What the base case of the function is.
#
#
# 4) How do we put data into a function call?
#  Set a variable 
#
# 
# 5) How do we get data out of a function call?
#  Return
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 2
#a2 = 2
#a3 = -1

#b1 = 2
#b2 = 0
#b3 = 4

#c1 = 3
#c2 = 4
#c3 = 5

#d1 = 5
#d2 = 7
#d3 = 5

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def check(numb,avg):
    if int(numb) == 1 or int + 2:
        avg += int(numb)
        user(avg)

def user(avg):
    numb = raw_input("Next:")
# Base case
    if numb == "":
        check(numb,avg)        
        print "The average of your odd numbers was {}".format(avg)
# Recursive case
    else:
        check(numb,avg)
        user(avg)

def main():
    avg = 0
    user(avg)
main()
