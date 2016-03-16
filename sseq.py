import re;s=lambda x,y:re.search('.*'.join(x),y)
fin=open("rosalind_sseq.txt","r")
fout=open("rosalind_sseq_ans.txt","w")
read=''.join(fin.read().split("\n"))
string=read.split(">")[1]
string=string[13:]
subseq=read.split(">")[2]
subseq=subseq[13:]
l=[]
flag=True
pos=-1
print string,subseq

for i in range(len(subseq)):
    if not flag:
        break
    pos=string.find(subseq[i],pos+1)
    if not pos==-1:
        l.append(pos+1)
        flag=True
    else:
        flag=False
        
print(l)
fout.write(str(l).strip("[").strip("]").replace(",",""))
fin.close()
fout.close()