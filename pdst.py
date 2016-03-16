import timeit

fin=open("rosalind_pdst.txt","r")
fout=open("rosalind_pdst_ans.txt","w")
ferr=open("rosalind_pdst_ans_complexity.txt","w")

def read():
  curr=""
  s=[]
  for line in fin.readlines():
    if line[0]==">":
      if curr !="":
	s.append(curr)
	curr=""
    else:
      curr+=line.strip("\n")
  if curr!="":
    s.append(curr)
    
  return s

def p_distance(x,y):  
  count=int(0)  
  for k in range(0,len(x)):    
    if x[k]!=y[k]:
      count+=1
      
  return float(count)/len(x)

strings=read()
n=len(strings)
D=[]
def solve():
  global D
  for i in range(0,n):
    l=[]
    for j in range(0,n):
      l.append(float(0.00000))
    D.append(list(l))

  for i in range(0,n):
    for j in range(0,i+1):
      if i==j:
	D[i][j]=0.00000
      else:
	D[j][i]=D[i][j]=p_distance(strings[i],strings[j])

t=timeit.Timer(solve)
ferr.write(str(t.timeit(1)))
for i in range(0,n):
  for j in range(0,n):
    fout.write("%.5f"%D[i][j]+" ")
  fout.write("\n")  
print D

fout.close()
fin.close()
ferr.close()      
  
