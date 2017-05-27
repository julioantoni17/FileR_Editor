from os.path import isfile
PROMPT = "> "

def write(file):
	try:
		while True:
			if isfile(file) == False:
				while True:
					print "\n\t\t\tThat is not a file or is not exists!!!"
					file = raw_input("\n--> Enter a file " + PROMPT)
					if isfile(file) == True:
						break
					else:
						continue
			else:
				break

		fileTW = open(file, 'r')
		INDATA = fileTW.read()
		fileTW.close()

		fileTW = open(file,'r+')
		NEWTEXT = raw_input("\n--> Enter a text " + PROMPT)
		fileTW.write(INDATA + "\n" + NEWTEXT)
		fileTW.close()

		fileTW = open(file, 'r')
		INDATANEW = fileTW.read()
		fileTW.close()

		add_more = raw_input("\n\t\t\tDo you want to add something more? (y/n) " + PROMPT)
		if add_more == "Y" or add_more == "y":
			MORETEXT = raw_input("\n--> Enter a text " + PROMPT)
			fileTW = open(file,'w')
			fileTW.write(INDATANEW + "\n" + MORETEXT)
			fileTW.close()
		else:
			exit()

	except KeyboardInterrupt:
		print "\n\t\t\tStopped by the user!"
