import timeit
from math import factorial

fin=open("rosalind_mmch.txt","r")
fout=open("rosalind_mmch_ans.txt","w")
ferr=open("rosalind_mmch_ans_complexity.txt","w")

s=''.join(fin.read().split("\n")[1:])
res=int(0)

def solve():
  global res
  a=s.count("A")
  u=s.count("U")
  g=s.count("G")
  c=s.count("C")
  res=(factorial(max(a,u))/factorial(max(a,u)-min(a,u)))*(factorial(max(g,c))/factorial(max(g,c)-min(g,c)))  
   
t=timeit.Timer(solve)
ferr.write(str(t.timeit(1)))
fout.write(str(res))
print res

fout.close()
fin.close()
ferr.close()  

  


