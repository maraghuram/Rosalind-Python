fin=open("rosalind_tran.txt","r")
fout=open("rosalind_tran_ans.txt","w")
read=fin.read()
s1=read.split(">")[1]
s2=read.split(">")[2]

s1=''.join(s1.split("\n")[1:])
s2=''.join(s2.split("\n")[1:])

transitions=transversions=0
print s1
print s2
def similar(x):
    if x=="A":
        return "G"
    elif x=="G":
        return "A"
    elif x=="C":
        return "T"
    else:
        return "C"
    

for i in range(len(s1)):
    if s1[i]==similar(s2[i]):
        transitions+=1
    elif not s1[i]==s2[i]:
        transversions+=1
res=float(transitions)/transversions        
print res
fout.write(str(res))
fin.close()
fout.close()