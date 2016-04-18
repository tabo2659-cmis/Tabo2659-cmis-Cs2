def txt():
    print """ 
This program will ask you for 5 integers or float values.
It will calculate the average of all values from 0 inclusive to 10 exclusive.
It will print out whether the resulting avergae is even or odd. 
"""
def avg(n0,n1,n2,n3,n4):
    average = float((n0 + n1 + n2 + n3 + n4))/2    
    return average

def zerototen(n0,n1,n2,n3,n4):
    if n0 > 10 or n0 < 0:
        return " {} is out of range ".format(n0)
    elif n1 > 10 or n1 < 0:
        return " {} is out of range ".format(n1)
    elif n2 > 10 or n2 < 0:
        return " {} is out of range ".format(n2)
    elif n3 > 10 or n3 < 0:
        return " {} is out of range ".format(n3)
    elif n4 > 10 or n4 < 0:
        return " {} is out of range ".format(n4)
    else:
        return " Hi "

def output(normavg, intavg, ):
    print """ 
The average is {}
The integer part of the average is {}
The integer part is {} """.format(normavg,intavg,)
     
def main(): 
    txt()
    n0 = raw_input(" n0: ")
    n1 = raw_input(" n1: ")
    n2 = raw_input(" n2: ")
    n3 = raw_input(" n3: ")
    n4 = raw_input(" n4: ")
    number = zerototen(n0,n1,n2,n3,n4)
    normavg = avg(n0,n1,n2,n3,n4)  
    intavg = int(avg(n0,n1,n2,n3,n4))

main()
