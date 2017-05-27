from os.path import isfile
PROMPT = "> "

def copy(FROM_FILE, TO_FILE):
	try:
		while True:
			if isfile(FROM_FILE) == False:
				while True:
					print "\n\t\t\tThat is not a file or is not exists!!!"
					FROM_FILE = raw_input("\n--> Enter a file " + PROMPT)
					if isfile(FROM_FILE) == True:
						break
					else:
						continue
			else:
				break


		OPEN_FROM_FILE = open(FROM_FILE,'r')
		INDATA = OPEN_FROM_FILE.read()

		OPEN_TO_FILE = open(TO_FILE,'w')
		WRITE = OPEN_TO_FILE.write(INDATA)

		OPEN_FROM_FILE.close()
		OPEN_TO_FILE.close()
		

	except KeyboardInterrupt:
		print "\n\t\t\tStopped by the user!"
