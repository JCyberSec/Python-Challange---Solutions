oldName = "channel/90052.txt"

def getFilename(fileName):
	for line in open(fileName):
		print (line)
		Num = line[16:]
		file = "channel/" + Num + ".txt"
		return file

for i in range(5000):
	newName = getFilename(oldName)
	oldName = newName