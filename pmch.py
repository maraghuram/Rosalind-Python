import math

fin=open("rosalind_pmch.txt","r")
fout=open("rosalind_pmch_ans.txt","w")

s=''.join(fin.read().split("\n")[1:])

AUcount=0
GCcount=0

for x in s:
  if x=="A" or x=="U":
    AUcount+=1
  elif x=="G" or x=="C":
    GCcount+=1
    
print math.factorial(AUcount/2)*math.factorial(GCcount/2)

fout.write(str(math.factorial(AUcount/2)*math.factorial(GCcount/2)))
fout.close()
fin.close()    