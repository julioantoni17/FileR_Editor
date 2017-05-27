from os.path import isfile
PROMPT = "> "

def delete(file):
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

		fileTD = open(file,'w')
		fileTD.truncate()
		fileTD.close()

	except KeyboardInterrupt:
		print "\n\t\t\tStopped by the user!"
