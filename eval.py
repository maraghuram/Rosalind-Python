import timeit
import math
from collections import Counter

fin=open("rosalind_eval.txt","r")
fout=open("rosalind_eval_ans.txt","w")
ferr=open("rosalind_eval_ans_complexity.txt","w")

n=int(fin.readline())
s=fin.readline()
gc=[float(x) for x in fin.readline().split()]
ans=[]

def solve():
    global ans
    count=Counter(s)
    for var in gc:
        res=(var/2)**(count['G']+count['C'])
        res*=((1-var)/2)**((count['A']+count['T']))
        ans.append(res*(n-1));

t=timeit.Timer(solve)
ferr.write(str(t.timeit(1)))
for x in ans:
    fout.write("%.3f"%x+" ")
    
fin.close()
fout.close()
ferr.close()
