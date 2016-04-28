def adder(summation,biggest):
    if float(numb) > float(numb):
        biggest += float(numb)

def adder(summation,biggest):
    numb = raw_input("Next Number:")    
    if numb == "":
        print "The greatest is {}".format(str(biggest)) 
    else:
        summation += float(numb)
        print "Running total: {}".format(str(summation))
        adder(summation)        
        
def main(): 
    summation = 0
    biggest = 0
    adder(summation,biggest)

main()
