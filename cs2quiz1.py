#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#The sign "=" is called the assignment operator and in python it is used to assign a value to a variable.
#
#
#2 3pts) Write a technical definition for 'function'
#A function is a specific named sequence of instructions/statements that performs a calculation.
#
#
#3 1pt) What does the keyword "return" do?
#Return gives the final output or value of a function and is used inside a function as the last statement. 
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: int = 4,-5
#	2: float = 4.5, 5.67
#	3: str = " Hello am I doing good? " , " did I get any wrong no hopefully "
#	4: bool = True,False
#	5: tupple = (" I " , " am " , 14.12 , " years old"),(" There are ", 4 , "people in my ", "family")  
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#A function defintion is naming a new function and the calcution it does according to the statements given to it. But a function call is calling an already defined function to perform a calculation and present the result it's supposed to give you.
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:input
#	2:process
#	3:ouput
#In input the computer recieves commands. In process it takes the information and performs a calculation of some sort. In output it presents the final result of it's calculation.
# 
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math
def radiusOfcircle1(a):
    r = math.sqrt(a/math.pi)
    return r

def radiusOfcircle2(b):
    r = math.sqrt(b/math.pi)
    return r

def radiusOfcircle3(c):
    r = math.sqrt(c/math.pi)
    return r

def main():
    C1 = int(raw_input("Area of C1:"))
    C2 = int(raw_input("Area of C2:"))
    C3 = int(raw_input("Area of C3:"))
    D1 = radiusOfcircle1(C1)
    D2 = radiusOfcircle2(C2)
    D3 = radiusOfcircle3(C3)
 
    print """ Circle        Diameter             
  C1           {}
  C2           {}
  C3           {}""".format(D1, D2, D3) 
main()
                             
