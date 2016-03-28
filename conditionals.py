#My conditional program will run the user through a day of school life. It will give the users options in the beginning they will be given three options to choose which will determine when they arrive at school(they won't know the value of the options until chosen). After that the user will be able to decide her/his day with different options given to them(some of whose value they will and some which they wont). The different options may be items that the user can eat for lunch and how they can answer the teacher in class, how they talk to their friends(which conversation occurs an how the conversation carries on in the game will rely on the users input and previous choices), stuff like that. Depending on their grade, which will be inputted by the user, the teachers will be determined. Depending on the choices they make during the day they either will or will not go to Mr. Souza's office.

import random
import math
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
        anotherchoice = raw_input("Your friend leaves for P.E do you attend the next period - Math or skip it as well?:(type skip or no):")
        if anotherchoice == "skip":
            consequence = """You sleep in the library till lunchbreak and your teachers see you
They inform your parents who inform Mr.Souza(R.I.P = You)
You are given a punishment to clean the lunch sala for 2 weeks"""
            
            print """ {} - not that bad I would say! 
THE END(You had a bad day)""".format(consequence)
        elif anotherchoice == "no":
            print """You go to your first class - English"""
        else:
            print "type one of the options"
    elif choose == "no":
        print """Wow your Goody two-shoes!
your friend joins you and both of attend first period - English"""
    else:
        print "type the options"
def duringEng():
    Classbehav = raw_input("Somebody tries to talk to you during class do you start a conversation?:")
    if Classbehav == "yes":
        print """Ms.Brill's makes fun of you for talking! - You feel embarassed
And now after english the 15 min break begins!""" 
    elif Classbehav == "no":
        print """ You say no and get through the class without any problem!
And now after english the 15 min break begins!"""
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
    elif arrival == "choice2" or "choice3":
        print "You take a seat and Ms.Brill's asks for your homework you haven't done it!"
    else:
        print "cooperate"
    
    if arrival == "choice2" or "choice3":
        print duringEng()
    else:
        print " cooperate"

def shortbreak():
    timespent = raw_input("Do you spend the break eating,talking or studying?:")
    if timespent == "talking":
        print "You have a nice conversation"
    elif timespent == "eating":
        print """your friends look at you and call you a hungry bastard
You have a good laugh about it"""
    elif timespent == "studying":
        print "Youre friends join you while studying"
    else:
        "You do nothing, JUST NOTHING"
def mathquestion():
    Rnumber1 = float(random.random())
    Rnumber2 = float(random.randint(15.0,20.0))
    Rnumber3 = float(random.choice([1,2234,3,3453]))
    print str({} + math.sqrt(({})**2 - 4*(48.0)*({}))/(2*{})).format(Rnumber1,Rnumber1,Rnumber2,Rnumber3)

def period2():
    print """ After English you go to your next class Math 
Ms.Rachna gives the class a question to get their brains working
the person to finish it first gets NOTHING! """
    question = mathquestion()    
    print question 
    answer = raw_input("Answer the question if you dare!, Type a number or type I GIVE UP:") 
    if answer == "I GIVE UP":
        print "Ms.Rachna says I didn't expect you to try anyways"  
    else:
        print """The smart kid who everyone hates for no reason got it right!
You hate him even more
class finishes and ou move on to your next period """
    
def period3(grade):
    if grade == "9":
        print """You sleep during health.....
        z
       z 
      z
(~.~)z """
    elif grade == "10":
        print """ You sleep during Com-sci.....
        z
       z 
      z
(~.~)z    wait..... Isn't that the class your in right now!? """
    elif grade == "11":
        print """ You sleep during your planning period.....
        z
       z
      z
(~.~)z """
    elif grade == "12":
        print """ You sleep during A.P Psyche.....
        z
       z 
      z
(~.~)z 
(at least you try to but Ms.Mildred keeps waking you up)
(O.O)"""
    else:
        print "LOL"
        
def period4(fitOrNot,gender): 
    if gender == "male":
        ouch = "Balls"
    elif gender == "female":
        ouch = "Breasts"
    else:
        print "this was hard work so cooperate!"
        
    print "You barely make it to your next class P.E because you were sleeping in the previous class"
    if fitOrNot == "yes":
        print """You played Basketball today and scored 10 HOOPS!! 
You feel more confident about yourself"""        
   
    elif fitOrNot == "no":
        print """ You got fainted during P.E and went to the nurses!"
You were in a coma and woke up 2 days later
You have a boyfriend now? Whaaaat!?
        
THE END(You found true love)
P.S Doesn't matter if youre a boy or girl you got a boyfriend"""
        
    elif fitOrNot == "YEES":
        print """You play football(Soccer) today and get 4 goals!
High-five! (jk you suck those were lucky shots)"""
   
    elif fitOrNot == "NOOOOOOO":
        print """ You were playing football and your mind was somewhere else
You get hit in the {} with the ball""".format(ouch)
    else:
        print "Hey :)"

    print "You finish P.E take a shower and go to eat lunch!(You must be so happy)"    

def lunch(gender):
    if gender == "male":
        hormones = " girls play basketball, if you know what i mean ;) "
    elif gender ==  "female":
        hormones = " boys play basketball, if you know what i mean ;) "
    else:
        print "in getting bored of these else's"
        
    location = raw_input("Where do you eat with your friends?(stone tables, cafeteria, lunch sala):")
    if location == "stonetables":
        print """ You go to the bathroom in the library 
and see Jon, Tabo and Bryson playing smash like they always do 
You enter the bathroom
The door of the bathroom suddenly closes
You see something, almost like a ghost in the corner
..............................
..................................
.....................................
.............AhhhhhhhhhhhHHHHHHHHHHHHHHHHHHH!!
..
...
.... -(O.O)- (In case you didn't realize that's the ghost)
        
You were never heard from again
THE END(You were killed by a ghost)"""
    
    elif location == "lunchsala:":
        print " You talk with your friends and enjoy the {}".format(hormones)
    elif location == "cafeteria":
        print " You talk and have fun with your friends!"
    print """ Your tired and the next class you have is Science 
(-_-) = boredom """

def chemlab(gender):
    if gender == "female":
        effect = "you end up going to prom with him later"
    elif gender == "male":
        effect = "you both become bro's and he helps you out during some hard times in life"
    else:
        print "lol"
        
    print """You are doing a bit of a dangerous lab experiment in class today
One of your friends gets injured - acid burns his arm badly"""
    friend = raw_input("Do you accompany him to the nurses?:")
    if friend == "yes":
        print """You missyour last period but your friendship grow stronger

THE END(You had a good day)
P.S {} """.format(effect)
    elif friend == "no":
        print "you continue on with your day"
    else:
        print "cooperate"
    
def period5(grade,gender):
    print""" You go to the science classroom 
    Your science picks on you for some reason and asks you these questions""" 
    if grade == "9":
        question = raw_input("What noble gas is not like the other noble gases?:")
        if question == "helium":
            print "You got it right! You got some candy!"
        else:
            print "Nooo that's wrong sorry no candy for you"
    elif grade == "10":
        question = raw_input("What is being cycled between cellular respiration and photosynthesis?:")
        if question == "matter":
            print "You got it right! You got some candy!"
        else:
            print "Nooo that's wrong sorry no candy for you"
    elif grade == "11":
        question = raw_input("Which of these is an element used for the Haber process?:")
        if question == "hydrogen":
            print "You got it right! You got some candy!"
        else:
            print "Nooo that's wrong sorry no candy for you"        
    elif grade == "12":
        question = raw_input("What is the name of the region where icy bodies that lie beyond Neptune's orbit?:")
        if question == "kuiper belt":
            print "You got it right! You got some candy!"
        else:
            print "Nooo that's wrong sorry no candy for you"
    else:
        print "cooperate"
    
    print chemlab(gender)

def period6(grade):
    print """ You reach your last class of the day - History
You have a history quiz today"""
    memory = raw_input("Did you remember you had a history test today?:")
    if memory == "yes":
        print """It's just a small test with 5 questions
You feel extremely confidenet in your answers"""
    elif memory == "no":
        print "even though you didn't remember you feel confident about the test"
    else:
        print "type what I told you to!"
    print "you get through class peacefully"
    
def afterschool():
    aftermath = raw_input("Are you part of any after school club?:")  
    if aftermath == "yes":
        print """You stay in school till 4:00 pm and go home later

THE END(You had an average day)"""
    elif aftermath == "no":
        print """ You spend a little time with your friends and then go home

THE END(You had an average day)"""

def main():
    grade = raw_input("Which grade are you in?:")
    gender = raw_input("Are you male or female?:")
    fitOrNot = raw_input("Are you good at sports?, Type yes or no or YEESS or NOOOOOOO(count the zeros or the program won't work sry):")
    arrival = raw_input("Pick one of these choice1,choice2,choice3 your choice will determine what time you arrive at school:")
    arrived = schooltime(arrival)
    firstp = period1(arrival)
    interval = shortbreak()
    secondp = period2()
    thirdp = period3(grade)
    fourthp = period4(fitOrNot,gender)
    fifthp = period5(grade,gender)
    sixthp = period6()
    
main()




