def hrslefttolive(yourage):
	hrs = (int(yourage) * 8760)
	return hrs

def timeleft(yourage):
	Functioncall = hrslefttolive(yourage)
        timeLeftforyou = (621960 - float(Functioncall))
	return timeLeftforyou


def output(yourname,grammar,desires,hrslefttolive,timeleft):
	 return " Hey! {} who {] how are you? I'm guessing you said yes to the Ferrari {] you did didn't you? " + " if you didn't why not!? Anyways you have lived for exactly {] hours to this day on this beautiful planet and you only have {} left to live.....................GET A FERRARI!!!! thank you for answering these utterly meaning less questions! :) ".format(yourname,grammar,desires,hrslefttolive,timeleft)

def main(): 
	yourage = raw_input("Type your age:")
	yourname = raw_input("Type your name:")
	grammar = raw_input("Type a verb in present continious tense:")
	desires = raw_input("Do want a FERRAI!!??:")
	timeleftforyou = str(timeleft(yourage))
	hrsleftotlive = str(hrslefttolive(yourage))	
	return output(yourname,grammar,desires,hrslefttolive,timeleft)
         
main()
        

	 
		
