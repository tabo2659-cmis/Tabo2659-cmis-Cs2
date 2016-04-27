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

def adder(summation):
    numb = float(raw_input("Next Number:"))        
    if numb == "":
        print "The sum is {}".format(summation) 
    elif numb == float:
        print numb 
    else:
        summation += float(numb)
        print "Running total: {}".format(summation)
        adder(summation)
        
def main(): 
    adder(0)

main()
