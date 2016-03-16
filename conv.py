import timeit

fin=open("rosalind_conv.txt","r")
fout=open("rosalind_conv_ans.txt","w")
ferr=open("rosalind_conv_ans_complexity.txt","w")

s1=[float(x) for x in fin.readline().split()]
s2=[float(x) for x in fin.readline().split()]

def solve():
  table=dict()
  for i in range(len(s1)):
    for j in range(len(s2)):
      diff=float("%.5f"%(s1[i]-s2[j]))
      if not diff in table:
	table[diff]=1
      else:
	table[diff]+=1
	
  x,multiplicity=0,0
  
  for key,val in table.items():
    if val>multiplicity:
      multiplicity=val
      x=key
      
  fout.write(str(multiplicity)+"\n"+str(x))

timer=timeit.Timer(solve)
ferr.write(str(timer.timeit(1)))

fin.close()
fout.close()
ferr.close()

