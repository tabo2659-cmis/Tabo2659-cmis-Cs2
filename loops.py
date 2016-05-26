#def countup(x):
#    while x >= 0:
#    	print x
#    	x -= 1
#countup(7)

#def countdown(y):
#    while y <= 10:
#    	print y
#    	y += 1
#countdown(6)

#def count(t):
#    while t > 0:
#        print t
#        t -= 1
#    while t < 0:
#        print t
#        t += 1
#count(-11)

#def countfrom2(x,y):
#    while x <= y:
#        print x
#        x += 1
#    while x >= y:
#        print x
#        x -= 1
#countfrom2(8,2)

def addodds(n):
    sum_ = 0
    if n < 0:
        while n < 0:
            if n % 2 != 0:
                sum_ += -n
                n += 1
    elif n > 0:
        while n < 0:
            if n % 2 != 0:
                sum_ += n
                n -= 1
    print sum_    
addodds(12)    
