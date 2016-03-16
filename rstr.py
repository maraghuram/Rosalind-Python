import math
import timeit

fin=open("rosalind_rstr.txt","r")
fout=open("rosalind_rstr_ans.txt","w")
ferr=open("rosalind_rstr_ans_complexity.txt","w")

l=fin.readline().split()
N=int(l[0])
x=float(l[1])
s=fin.readline().strip("\n")
res=0.0

def solve():
    global res   
    x1=math.log(x/2.0)
    x2=math.log((1.0-x)/2.0)
    for i in range(0,len(s)): 
        if s[i]=="G" or s[i]=="C" :
            res+=x1    
        elif s[i]=="A" or s[i]=="T":
            res+=x2
    res=math.exp(res)
    res=1.0-res
    res=math.pow(res,N)
    res=1.0-res
    
t=timeit.Timer(solve)
ferr.write(str(t.timeit(1)))
fout.write("%.3f"%res)
fin.close()
fout.close()
ferr.close()
