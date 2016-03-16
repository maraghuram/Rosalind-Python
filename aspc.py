import timeit
from math import factorial

fin=open("rosalind_aspc.txt","r")
fout=open("rosalind_aspc_ans.txt","w")
ferr=open("rosalind_aspc_ans_complexity","w")

l=fin.read()
a=int(l.split(" ")[0])
b=int(l.split(" ")[1])
res=int(0)
MOD=1000000

def nCk(n,k):
  return (factorial(n)/(factorial(k)*factorial(n-k)))%MOD

def solve():
    global MOD
    global res
    
    for i in range(b,a+1):
	res=(res+nCk(a,i))%MOD	
	
t=timeit.Timer(solve)
ferr.write(str(t.timeit(1)))
print res
fout.write(str(res))


fin.close()
ferr.close()
fout.close()
