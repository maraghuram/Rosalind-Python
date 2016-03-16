fd=open("rosalind_dna.txt","r")
l=fd.readlines()
a=g=c=t=int(0)

for var in l[0]:
	if var=="A":
		a+=1
	elif var=="G":
		g+=1
	elif var=="C":
		c+=1
	elif var=="T":
		t+=1
print a," ",c," ",g," ",t
					
