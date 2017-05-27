from os.path import exists, isfile
PROMPT = "> "

def read(file):
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

		fileTR = open(file,'r')
		print fileTR.read()
		while True:
			read_more = raw_input("\n\t\t\tDo you want to read one more file? (y/n) " + PROMPT)
			if read_more == "Y" or read_more == "y":
				while True:
					if exists(file) == False:
						print "\n\t\t\tFile not found!"
						file = raw_input("\n--> Enter a file " + PROMPT)
					else:
						break

				fileTR = open(raw_input("\n--> Enter a file " + PROMPT),'r')
				print fileTR.read()
				fileTR.close()
			else:
				fileTR.close()
				break

	except KeyboardInterrupt:
		print "\n\t\t\tStopped by the user!"
