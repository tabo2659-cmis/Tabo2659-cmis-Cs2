def countup(n):
    if n >= 10:
        print "Blastoff!!"
    else:
        print n
        countup(n+1)

def main():
    countup(1)

main()

def countdown_from_to(start,stop):
    if start == stop:
        print "Blastoff!!"
    elif start <= stop:
        print "Invalid Pair"
    else:
        print start
        countdown_from_to(start - 1,stop)

def main():
        countdown_from_to(16,32) 
main()

def adder(sum_):
    print sum_
    numb = raw_input("Next Number:")    
    if numb == None:
        print "The Sum Is {}".format(sum_) 
    else:
        adder(sum_)
        
def main():
    sum_ = "Running Total:0"
    adder(sum_)
main()
