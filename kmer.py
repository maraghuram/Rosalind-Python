fin=open("rosalind_kmer.txt","r")
fout=open("rosalind_kmer_ans.txt","w")
base="ACGT"
count=dict()
res=[]

def combs(x,h):
    if h==4:
        res.append(str(x))
        return
    for b in base:
        combs(x+b,h+1)
        
def findAll(x,y):
    count=0
    i=0
    while i<len(y):
        i=y.find(x,i)
        if i==-1: break
        count+=1
        i+=1
    return count
        
combs("",0)        
string=''.join(fin.read().split("\n")[1:])

for r in res:
    val=findAll(r,string)
    print val
    fout.write(str(val)+" ")

fin.close()
fout.close()