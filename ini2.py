fd=open("rosalind_ini2.txt","r")
line=fd.read().strip("\n")
res=int(0)
for var in line.split(" "):
	res=res+(int(var)*int(var))
print res	
