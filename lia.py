import math

def binomial_coff(m,n):
  return math.factorial(m)/(math.factorial(m-n)*math.factorial(n))

fin=open("rosalind_lia.txt","r")
fout=open("rosalind_lia_ans.txt","w")
s=fin.read().split(" ")
k=int(s[0])
n=int(s[1])
lim=(1<<k)
res=0.0
for i in range(n,lim+1):
  res+=(binomial_coff(lim,i)*math.pow(0.25,i)*math.pow(0.75,lim-i))
print res
fout.write("%.3f"%res)
fout.close()
fin.close()
