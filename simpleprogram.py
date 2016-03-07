def hrslived(yourage):
	hrs = (int(yourage) * 8760)
	return hrs

def timeleft(yourage):
	Functioncall = hrslived(yourage)
        timeLeftforyou = (621960 - int(Functioncall))
	return timeLeftforyou


def output(yourname,grammar,desires,function1,function2):
	 return """ Hey! {} who {} how are you? I'm guessing you said yes to the Ferrari {} you did didn't you? if you didn't why not!? Anyways you have lived for exactly {} hours to this day on this beautiful planet and you only have {} left to live.....................GET A FERRARI!!!! thank you for answering these utterly meaning less questions! :) """.format(yourname,grammar,desires,function1,function2)

def main(): 
	yourage = raw_input("Type your age:")
	yourname = raw_input("Type your name:")
	grammar = raw_input("Type a verb in present continious tense:")
	desires = raw_input("Do want a FERRAI!!??:")
	function1 = str(hrslived(yourage))	
	function2 = str(timeleft(yourage))
	return output(yourname,grammar,desires,function1,function2)
         
print main()
        

	 
		
