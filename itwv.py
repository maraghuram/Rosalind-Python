import timeit
fin=open("rosalind_itwv.txt","r")
fout=open("rosalind_itwv_ans.txt","w")
ferr=open("rosalind_itwv_ans_complexity.txt","w")

s=fin.readline().strip()
patterns=[x.strip() for x in fin.readlines()]
M=[]

def check(x,y,z):
  if len(z)==0:
    return True
    
  if len(x)>0 and len(y)>0 and x[0]==y[0]==z[0]:
    return check(x[1:],y,z[1:]) or check(x,y[1:],z[1:])
  elif len(x)>0 and x[0]==z[0]:
    return check(x[1:],y,z[1:])
  elif len(y)>0 and y[0]==z[0]:
    return check(x,y[1:],z[1:])
  else :
    return False
    
def solve():
  global M
  for i in range(len(patterns)):
    L=[]
    for j in range(len(patterns)):
      reqLength=len(patterns[i])+len(patterns[j])
      maxIndex=len(s)-reqLength+1
      flag=False
      for k in range(maxIndex):
	flag=check(patterns[i],patterns[j],s[k:k+reqLength])
	if(flag):
	  break
      L.append(1 if flag else 0)
    M.append(L)    
    
timer=timeit.Timer(solve)
ferr.write(str(timer.timeit(1)))
print M
fout.write(str(M).replace("], ","\n").replace("[","").replace("]","").replace(",",""))

fin.close()
fout.close()
ferr.close()