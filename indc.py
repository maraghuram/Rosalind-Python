import timeit
import math

def comb(n,r):
  return float(math.factorial(n))/float(math.factorial(n-r)*math.factorial(r))

fin=open("rosalind_indc.txt","r")
fout=open("rosalind_indc_ans.txt","w")
ferr=open("rosalind_indc_ans_complexity.txt","w")

def solve():
	n=int(fin.read())*2
	exact=[0.0]*(n+1)
	for i in range(n+1):
		exact[i]=math.log10(comb(n,i))+(n*math.log10(0.5))
  
	atleast=[0.0]*(n+1)
	tot=float(0.0)

	for i in range(n,0,-1):
		tot+=(10.0**exact[i])
	    	atleast[i]=math.log10(tot)
		print "%.3f"%math.log10(tot)
  
	for i in range(1,n+1):
	  	fout.write(str(atleast[i])+" ")

timer=timeit.Timer(solve)
ferr.write(str(timer.timeit(1)))

fin.close()
ferr.close()
fout.close()
