import math
def add(a,b):
	return a + b

add(3,4)
#A function that adds some numbers
def sub(a,b):
	return a - b

sub(5,3)
#A function that subtracts some numbers 
def mul(x,y):
	return x*y

mul(4,4)
#A function that multiplys some numbers
def div(g,h):
	return g/h

div(2,3.0)
#A function that divides some numbers 
def SecsToHours(a,b,c):
	return a/b/c

SecsToHours(86400,60,60) 
#A function that converts number of seconds into hours
def Areaofacircle(r):
	pi = (math.pi)
	return pi * r**2
	
Areaofcircle=(5)
#A function that tells the area of a circle
def Volumeofsphere(r):
	pi = (math.pi)
	return (((4/3.0)*pi)*r**3)

Volumeofsphere=(5)
#A function that tells the volume of a sphere
def averagevolume(a,b):
	pi = (math.pi)
	x = a/2
	y = b/2
	Vol1 = (((4/3.0)*pi)*a**3)
	Vol2 = (((4/3.0)*pi)*b**3)
	return (Vol1 + Vol2)/2

averagevolume(10,20)
#A function that tells the average voulume of two spheres
def areaoftriangle(a,b,c):
	p = a+b+c/2.0
	return math.sqrt(p*(p-a)*(p-b)*(p-c))

print areaoftriangle(1,2,2.5)
#A function that tells the area of a triangle
def right_align(a):
	return (a.rjust(80))
right_align("Hello")
#A function that aligns hello to the right side of python
def center(a):
	return (a.center(40))
center("Hello")
#A function that aligns hello to center of python
def msgbox(a):
    return "+" + (len(a) + 4) * "-" + "+\n" "|" + "  " + a + "  " + "|\n" "+" + (len(a) + 4) * "-" + "+"

msgbox("Hello")
msgbox("I eat cats")
# This function displays the word Hello and the statement I eat cats in a box

A = add(3,4)
B = sub(5,3)
C = mul(4,4)
D = div(2,3.0)
E = SecsToHours(86400,60,60)
F = Areaofcircle=(5)
G = Volumeofsphere=(5)
H = averagevolume(5,10)
I = areaoftriangle(1,2,2.5)
J = right_align("Hello")
K = center("Hello")
L = msgbox("I eat cats!")
# Stores all the functions in this file in a variable


