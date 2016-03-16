import timeit
from Bio import Phylo
from StringIO import StringIO

fin=open("rosalind_ctbl.txt","r")
fout=open("rosalind_ctbl_ans.txt","w")
ferr=open("rosalind_ctbl_ans_complexity.txt","w")

def clean(l):
  res=[x.name for x in l if not x.name==None]
  return res

def solve():
	text=fin.read().strip("\n")
	tree=Phylo.read(StringIO(text),'newick')
	allLabels=tree.get_nonterminals()+tree.get_terminals()
	goodLabels=clean(allLabels)
	goodLabels.sort()
	print goodLabels

	splits=tree.get_nonterminals()
	subsets=[]
	for split in splits:
	    subtree=split.get_nonterminals()+split.get_terminals()
	    if len(subtree)==1 or len(subtree)>=len(allLabels)-1:
	      continue
	    clades=clean(subtree)
	    bits=[None]*len(goodLabels)
	    for y in clades:
	      bits[goodLabels.index(y)]=1
	    for i in range(len(bits)):
	      if bits[i]==None:
		bits[i]=0
	    subsets.append(bits)

	print subsets
	fout.write(str(subsets).replace("], ","\n").replace("[","").replace("]","").replace(", ",""))
	
t=timeit.Timer(solve)
ferr.write(str(t.timeit(1)))
fin.close()
fout.close()
ferr.close()

