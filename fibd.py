fin=open("rosalind_fibd.txt","r")
fout=open("rosalind_fibd_ans.txt","w")
line=fin.read().strip("\n")
line=line.split(" ")
n=int(line[0])
m=int(line[1])

memo=111*[int(0)]
memo[0]=memo[1]=memo[2]=int(1)

for i in range(3,n+1):
  memo[i]=memo[i-1]+memo[i-2]
  if i>m:
    memo[i]-=memo[i-m-1]
  
fout.write(str(memo[n]))