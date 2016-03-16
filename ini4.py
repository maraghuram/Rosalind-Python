fd=file("rosalind_ini4.txt","r")
line=fd.read().strip("\n")
a=int(line.split(" ")[0])
b=int(line.split(" ")[1])
res=int(0)
for i in xrange(a,b+1):
	if i%2==1:
		res=res+i
print res		
