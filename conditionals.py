#My conditional program will run the user through a day of school life. It will give the users options in the beginning they will be given three options to choose which will determine when they arrive at school(they won't know the value of the options until chosen). After that the user will be able to decide her/his day with different options given to them(some of whose value they will and some which they wont). The different options may be items that the user can eat for lunch and how they can answer the teacher in class, how they talk to their friends(which conversation occurs an how the conversation carries on in the game will rely on the users input and previous choices), stuff like that. Depending on their grade, which will be inputted by the user, the teachers will be determined. Depending on the choices they make during the day they either will or will not go to Mr. Souza's office.

def schooltime(arrival):
    option1 = "You arrived late and missed first 5 mins of class"
    option2 = "You arrived right on time but forgot to do homework"
    option3 = "You arrived on time and are preapred for the day"
    if arrival == A:
        return option1
    elif arrival == B:
        return option2
    else:
        return option2

def main():
    arrival = raw_input("Pick one of these A,B,C your choice will determine what time you arrive at school")
    arrived = schooltime(arrival)
main()
