import timeit
from Bio import Phylo
from StringIO import StringIO

fin=open("rosalind_nkew.txt","r")
fout=open("rosalind_nkew_ans.txt","w")
ferr=open("rosalind_nkew_ans_complexity.txt","w")

newick_trees=fin.read().strip().split("\n\n")

def solve():

  for newick_tree in newick_trees:
    text,query=newick_tree.split("\n")
    u,v=query.split()
    tree=Phylo.read(StringIO(text),"newick")
    print int(tree.distance(u,v))
    fout.write(str(int(tree.distance(u,v)))+" ")

timer=timeit.Timer(solve)
ferr.write(str(timer.timeit(1)))

fin.close()
fout.close()
ferr.close()
