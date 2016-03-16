fd=open("rosalind_revc.txt","r")
l=fd.readlines()[0].strip("\n")
out=""
for var in l:
	if var=="T":
		out=out+"A"
	elif var=="G":
		out=out+"C"
	elif var=="A":
		out=out+"T"
	elif var=="C":
		out=out+"G"			
out=out[::-1]
print out		
