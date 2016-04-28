def great(summation,biggest,numb):
    if float(biggest) > float(numb):
        biggest += float(numb)
    else:
        print "Hi"

def adder(summation,biggest,numb):
    greatest = great(summation,biggest,numb)
    if numb == "":
        print "The greatest is {}".format(str(greatest)) 
    else:
        summation += float(numb)
        print "Running total: {}".format(str(summation))
        adder(summation,biggest,numb)        
        
def main(): 
    numb = raw_input("Next Number:")    
    summation = 0
    biggest = 0
    adder(summation,biggest,numb)

main()
