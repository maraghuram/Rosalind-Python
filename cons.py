fin=open("rosalind_cons.txt","r")
fout=open("rosalind_cons_ans.txt","w")
lines=fin.readlines()
matrix=list()
profile=list()
consensus=""
base=list("ACGT")
row=""

for line in lines:
	if line[0]==">": 
		if not row=="":
			matrix.append(list(row))
		row=""	
		continue
	line=line.strip("\n")
	row+=line		
matrix.append(list(row))
	
rows=int(len(matrix))
columns=int(len(matrix[0]))	
		
for x in range(0,4):
	count=list()
	for y in range(0,columns):
		sum=int(0)		
		for z in range(0,rows):
			if matrix[z][y]==base[x]:
				sum+=1
		count.append(sum)
	profile.append(list(count))
for i in range(0,columns):
	best=-1
	bestVal=-1
	for j in range(0,4):
		if profile[j][i] > bestVal:
			bestVal=profile[j][i]
			best=j
	consensus+=(base[best])

fout.write( consensus+"\n")
for i in range(0,4):
	fout.write(base[i]+":")
	for j in range(0,columns):
		fout.write(" "+str(profile[i][j]))			
	fout.write("\n")
