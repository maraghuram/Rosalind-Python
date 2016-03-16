import timeit
from StringIO import StringIO
from Bio import Phylo

fin=open("rosalind_nwck.txt","r")
fout=open("rosalind_nwck_ans.txt","w")
ferr=open("rosalind_nwck_ans_complexity.txt","w")

lines=[l for l in fin.read().strip("\n").split("\n\n")]
res=[]
def solve():
    for group in lines:
        text,nodes=group.split("\n")
        u,v=nodes.split()
        tree=Phylo.read(StringIO(text),'newick')
        res.append(int(tree.distance(u,v)))
        
t=timeit.Timer(solve)
ferr.write(str(t.timeit(1)))
fout.write(str(res).replace("]","").replace("[","").replace(",",""))
fin.close()
fout.close()
ferr.close()
