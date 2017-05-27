from os.path import exists
PROMPT = "> "

def create(file):
	try:
		while True:
			if exists(file) == True:
				print "\n\t\t\tFile already exists!"
				file = raw_input("\n--> Enter other file name " + PROMPT)
			else:
				break

		fileTC = open(file,'w')
		fileTC.write("")
		fileTC.close()

		create_more = raw_input("\n\t\t\tDo you want to create one more file? (y/n) " + PROMPT)
		if create_more == "Y" or create_more == "y":
			new_file = raw_input("\n--> Enter a file name " + PROMPT)
			while True:
				if exists(new_file) == True:
					print "\n\t\t\tFile already exists!"
					file = raw_input("\n--> Enter other file name " + PROMPT)
				else:
					break

			MORETC = open(new_file,'w')
			MORETC.write("")
			MORETC.close()
		else:
			exit()
	except KeyboardInterrupt:
		print "\n\t\t\tStopped by the user!"
