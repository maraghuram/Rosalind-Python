import math

fin=open("rosalind_prob.txt","r")
fout=open("rosalind_prob_ans.txt","w")
s=fin.readline().strip("\n")
A=fin.readline().strip("\n").split(" ")
for i in range(0,len(A)):
  A[i]=float(A[i])
B=[]

for j in range(0,len(A)):
  res=0.0
  x1=math.log10(A[j]/2.0)
  x2=math.log10((1.0-A[j])/2.0)
  for i in range(0,len(s)): 
    if s[i]=="G" or s[i]=="C" :
      res+=x1    
    elif s[i]=="A" or s[i]=="T":
      res+=x2
  B.append("%.3f"%res)
  fout.write(B[j]+" ")  
print B

fin.close()
fout.close()
  
  
