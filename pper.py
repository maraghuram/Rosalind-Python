fin=open("rosalind_pper.txt","r")
fout=open("rosalind_pper_ans.txt","w")
line=fin.read()
n=int(line.split(" ")[0])
k=int(line.split(" ")[1])
res=0

for i in range(n-k+1,n+1):
  res=(res*i)%1000000
print res
fout.write(str(res))  

fin.close()
fout.close()