import random
def check(number,randomN,rounds):
    if int(number) == randomN and rounds == 2 or 3:
        randomN = random.randint(0,100)
        attempts(rounds-1,randomN,tries=5)
    elif rounds <= 0:
        print " Thanks for playing "
    else:
        print " Thanks for playing "
def guess(rounds,randomN,tries):
    number = raw_input(" Guess a number: ")
    if int(number) == randomN:
        print "Thats Correct You must be a psychic"
        print "{} rounds remaining".format(rounds)        
        check(number,randomN,rounds)
    elif int(number) < randomN:
        print " That's too low "
        attempts(rounds,randomN,tries-1)
    elif int(number) > randomN:
        print " That's too high "
        attempts(rounds,randomN,tries-1)
    else:
        print " Hi, Im bored do you wanna play truth or dare? "

def attempts(rounds,randomN,tries):
    if rounds == 0 and tries == 0:
        print "Thanks for playing!"
        exit()
    if tries == 0:
        print "{} rounds remaining".format(rounds)
        tries = 5
        randomN = random.randint(0,100)
        guess(rounds-1,randomN,tries)
    else:
        guess(rounds,randomN,tries)
    
def main():
    print "Guess a number from 0 to 100 including 0 and 100"
    print "{} rounds remaining".format(3)
    randomN = random.randint(0,100)
    rounds = 2
    tries = 5
    attempts(rounds,randomN,tries)

main()
