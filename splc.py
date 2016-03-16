fin=open("rosalind_splc.txt","r")
fout=open("rosalind_splc_ans.txt","w")
cod=open("codon_table.txt","r")
lookup=dict()
for line in cod.readlines():
  line=line.strip("\n")
  i=int(0)
  pairs=line.split("  ")  
  for i in range(0,len(pairs)):
    if pairs[i]=="":
      continue
    key,val=pairs[i].split(" ")
    lookup[key]=val

fin.readline()
string=""
while True:
  line=fin.readline()
  if line[0]==">":
    break
  string+=line.strip("\n")
introns=[]
curr=""
for line in fin.readlines():
  if line[0]==">":
    if not curr=="":
      introns.append(curr)
      curr=""
    continue
  curr+=line.strip("\n")
  
if not curr=="":
  introns.append(curr)
  
res=""

for i in range(0,len(introns)):  
  string=string.replace(introns[i],"")  
  
string=string.replace("T","U")

for i in range(0,len(string)/3):  
  code=string[3*i:3*(i+1)]
  if lookup[code]=="Stop":
    break
  res+=lookup[code]  

fout.write(res+"\n")
print res

fin.close()
fout.close()  
cod.close()  

  
