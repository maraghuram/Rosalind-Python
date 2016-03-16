fd=open("rosalind_ini6.txt","r")
line=fd.read().strip("\n")
line=line.split(" ")
lookup=dict()
for word in line:
	if word in lookup:
		lookup[word]=lookup[word]+int(1)
	else:
		lookup[word]=int(1)
for key,value in lookup.items():
	print key.strip("\n")," ",value
