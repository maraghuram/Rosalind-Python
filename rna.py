fd=open("rosalind_rna.txt","r")
l=fd.readlines()[0].strip("\n")
out=""
for var in l:
	if var=="T":
		out=out+"U"
	else:
		out=out+var
print out				
