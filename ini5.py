fd=open("rosalind_ini5.txt","r")
lines=fd.readlines()
ptr=int(1)
for line in lines:
	if ptr%2==0:
		print line.strip("\n")
	ptr=ptr+1	
