def hrslefttolive(yourage):
	hrs = (int(yourage) * 8760)
	return hrs

def timeleft(yourage):
	z = hrslefttolive(yourage)
        g = (621960 - float(z))
	return g

def concan(x,a,b):
	return  " Hey! {} who {} how are you? I'm guessing you said yes to the Ferrari {} you did didn't you? ".format(x,a,b)

def main(): 
	yourage = raw_input("Type your age:")
	yourname = raw_input("Type your name:")
	grammar = raw_input("Type a verb in present continious tense:")
	desires = raw_input("Do want a FERRAI!!??:") 	
	return str(concan(yourname,grammar,desires)) + " if you didn't why not!? Anyways you have lived for exactly " + str(hrslefttolive(yourage)) + " hours to this day on this beautiful planet and you only have " +  str(timeleft(yourage)) + " left to live.....................GET A FERRARI!!!! thank you for answering these utterly meaning less questions! :) "         
print main()
        

	 
		
