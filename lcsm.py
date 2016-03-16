fin=open("rosalind_lcsm.txt","r")
fout=open("rosalind_lcsm_ans.txt","w")
strings=list()
lines=fin.readlines()
currstr=""
cnt=int(0)

for line in lines:
  line=line.strip("\n")
  if line[0]==">":
    if not currstr=="":
      cnt+=1
      strings.append(currstr)
    currstr=""
  else:
    currstr+=line

if not currstr=="":
  cnt+=1
  strings.append(currstr)
  
best=""
sz=len(strings[0])
for i in range(0,sz):
  for j in range(i,sz):
    sub=str(strings[0][i:j+1])
    #print sub
    flag=True
    for k in range(1,cnt):      
      if strings[k].find(sub) == -1 :
	flag=False
	break
    if flag and len(sub) > len(best):
      best=sub
fout.write(best)
fin.close()
fout.close()