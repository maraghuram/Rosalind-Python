fin=open("rosalind_orf.txt","r")
fout=open("rosalind_orf_ans.txt","w")

string=''.join(fin.read().split("\n")[1:])
fin.close()

table=open("codon_table.txt","r")
lookup=dict()
for line in table.readlines():
  line=line.strip("\n")
  i=int(0)
  pairs=line.split("  ")
  for i in range(0,len(pairs)):
    if pairs[i]=="":
      continue
    key,val=pairs[i].split(" ")
    lookup[key]=val
table.close()
reverse=""
for i in range(len(string)-1,-1,-1):
  if string[i]=="C":
    reverse+="G"
  elif string[i]=="G":
    reverse+="C"
  elif string[i]=="A":
    reverse+="T"
  else:
    reverse+="A"
	
strings=[string,reverse]
output=set()
for s in strings:
  for start in range(0,3):  
    sz=len(s)
    startList=[]
    for i in range(0,sz/3):
      read=s[3*i:3*(i+1)]
      if read=="ATG":
	startList.append(i)    
    for pos in startList:
      res=""
      for j in range(pos,sz/3):
	read=s[3*j:3*(j+1)]
	read=read.replace("T","U")
	code=lookup[read]
	if code=="Stop":	  
	  output.add(res)
	  break
	res+=code

    s=s[1:]
    
print output
for x in output:
  fout.write(x+"\n")
fout.close()
  