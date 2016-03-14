def numberRange(number1,number2):
    return random.randit(a,b)

def resultbyuser(result,usersGuess):
    if result > usersGuess:
        sub = usersGuess - result
        print "That's over by {}"
    else:
        add = usersGuess + result
        print "That's under by {}"

def main():
    number1 = int(raw_input("What is the minimum number?"))
    number2 = int(raw_input("What is the maximum number?"))
    print "Im thinking of a number from {} to {}".format(a,b)
    usersGuess = int(raw_input("What do you think it is?:"))
    result = int(numberRange(number1,number2))
    if result == usersGuess:
        print """The target was {}
Your guess was {}
That's correct! You must be a psychic!"""
    else:
        print """The target was {}
Your guess was {}
{}"""

