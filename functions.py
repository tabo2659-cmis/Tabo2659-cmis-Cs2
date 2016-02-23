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
def Areaofcircle(r):
	pi = (math.pi)
	return pi * r **2
	
Areaofcircle(5)
#A function that tells the area of a circle
def Volumeofsphere(r):
	pi = (math.pi)
	return (((4/3.0)*pi)*r**3)

Volumeofsphere(5)
#A function that tells the volume of a sphere
def averagevolume(a,b):
	pi = (math.pi)
	x = a/2
	y = b/2
	Vol1 = Volumeofsphere(int(x))
	Vol2 = Volumeofsphere(int(y))
	return (Vol1 + Vol2)/2

averagevolume(10,20)
#A function that tells the average voulume of two spheres
def areaoftriangle(a,b,c):
	p = (a+b+c)/2.0
	return math.sqrt(p*(p-a)*(p-b)*(p-c))

areaoftriangle(1,2,2.5)
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
    return "+" + (len(a) + int(4)) * "-" + "+\n" "|" + "  " + a + "  " + "|\n" "+" + (len(a) + int(4)) * "-" + "+"

msgbox("Hello")
msgbox("I eat cats")
# This function displays the word Hello and the statement I eat cats in a box

a = add(4,6)
b = add(8,6)
print msgbox(str(a))
print msgbox(str(b)) 
c = sub(5,3)
d = sub(4,4)
print msgbox(str(c))
print msgbox(str(d)) 
e = mul(2,3.0)
f = mul(4,8)
print msgbox(str(e))
print msgbox(str(f)) 
g = div(48,8)
h = div(625,25)
print msgbox(str(g))
print msgbox(str(h)) 
i = SecsToHours(46890,60,60)
j = SecsToHours(60000,60,60)
print msgbox(str(i))
print msgbox(str(j)) 
k = Areaofcircle(6)
l = Areaofcircle(9)
print msgbox(str(k))
print msgbox(str(l)) 
m = Volumeofsphere(7)
n = Volumeofsphere(14)
print msgbox(str(m))
print msgbox(str(n)) 
o = averagevolume(20,40)
p = averagevolume(40,60)
print msgbox(str(o))
print msgbox(str(p)) 
q = areaoftriangle(2,2,2)
r = areaoftriangle(4,2,6)
print msgbox(str(q))
print msgbox(str(r)) 
s = right_align("MEEEEE")
t = right_align("The end is nigh!")
print msgbox(str(s))
print msgbox(str(t)) 
u = center("Haundig")
v = center("Who wants to play CSGO?")
print msgbox(str(u))
print msgbox(str(v)) 
w = msgbox("Dragons dogma")
x = msgbox("Undertale")
print msgbox(str(w))
print msgbox(str(x)) 
# Stores all the functions in this file in a variablen




