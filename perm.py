import itertools
fin=open("rosalind_perm.txt","r")
fout=open("rosalind_perm_ans.txt","w")

n=int(fin.read())
l=list()
for i in range(1,n+1):
    l.append(i)
all=list(itertools.permutations(l))
fout.write(str(len(all))+"\n")
for perm in all:
    fout.write(str(perm).replace(",","").strip(")").strip("(")+"\n")
    
fin.close()
fout.close()    
