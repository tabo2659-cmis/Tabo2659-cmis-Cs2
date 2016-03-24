#My conditional program will run the user through a day of school life. It will give the users options in the beginning they will be given three options to choose which will determine when they arrive at school(they won't know the value of the options until chosen). After that the user will be able to decide her/his day with different options given to them(some of whose value they will and some which they wont). The different options may be items that the user can eat for lunch and how they can answer the teacher in class, how they talk to their friends(which conversation occurs an how the conversation carries on in the game will rely on the users input and previous choices), stuff like that. Depending on their grade, which will be inputted by the user, the teachers will be determined. Depending on the choices they make during the day they either will or will not go to Mr. Souza's office.
print "Answer all questions in yes or no answers unless an option is given"

def schooltime(arrival):
    if arrival == "choice1":
        print "You arrived late and missed first 5 mins of class but did your homework" 
    elif arrival == "choice2":
        print "You arrived on time but forgot to do some of your homework" 
    elif arrival == "choice3": 
        print "You arrived right on time and are preapred for the day"  
    else:
        print "type in the given order" 

def whattodo():
    choose = raw_input("You see a friend ditching class do you join him?:") 
    if choose == "yes":
        print "you skip first period - English"
        anotherchoice = raw_input("Your friend leaves for P.E do you attend the next period - Math or skip it as well?:")
        if anotherchoice == "yes":
            consequence = """You sleep in the library till lunchbreak and your teachers see you
They inform your parents who inform Mr.Souza(R.I.P = You)
You are given a punishment to clean the lunch sala for 2 weeks"""
            
            print """ {} - not that bad I would say! 
            THE END(You had a bad day)""".format(consequence)
        else:
            print """You go to your first class - English"""
    else:
        print """Wow your Goody two-shoes!
        your friend joins you and both of attend first period - English"""

def duringEng():
    Classbehav == raw_input("Somebody tries to talk to you during class do you start a conversation?:")
    if Classbehav == "yes":
        print "Ms.Brill's makes fun of you for talking! - You feel embarassed" 
    elif Classbehave == "no":
        print "You say no and get through the class without any problem!"
    else:
        print "cooperate"

def period1(arrival):
    if arrival == "choice1":
        print "because you were late you had to go and get a late slip"   
    elif arrival == "choice2" or "choice3":
        print "You go to your first class - English"
    else:
        print "plz cooperate!"
    
    if arrival == "choice1":
        print whattodo()  
    elif arrival == "choice2":
        print "You take a seat and Ms.Brill's asks for your homework you haven't done it!"
    else:
        print "cooperate"
    
    if arrival == "choice2" or "choice3":
        print duringEng()
    else:
        print " cooperate"

def main():
    arrival = raw_input("Pick one of these choice1,choice2,choice3 your choice will determine what time you arrive at school:")
    arrived = schooltime(arrival)
    firstp = period1(arrival)
    
main()
