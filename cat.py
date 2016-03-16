fin=open("rosalind_cat.txt","r")
fout=open("rosalind_cat_ans.txt","w")

s=''.join(fin.read().split("\n")[1:])
n=len(s)

def comp(x):
  if x=="A":
    return "U"
  elif x=="U":
    return "A"
  elif x=="G":
    return "C"
  elif x=="C":
    return "G"
  
dp=[]  
for i in range(0,n+1):
  l=[]
  for j in range(0,n+1):
    l.append(int(0))
  dp.append(list(l))  


print s

MOD=int(1000000)
dp[0][0]=int(0)
for i in range(1,n):
  dp[i][i+1]=int(1) if s[i-1]==comp(s[i]) else int(0)
for x in range(2,n+1):
  sz=2*x
  i=1
  while i+sz-1<=n:
    j=i+sz-1
    for k in range(i+1,j+1):
      if s[k-1]==comp(s[i-1]):
	if (k-i+1)%2==0 and (j-k)%2==0:
	  l=dp[i+1][k-1] if i+1<k-1 else int(1)
	  r=dp[k+1][j] if k+1<j else int(1)
	  dp[i][j]=(dp[i][j]+(l*r)%MOD)%MOD
	  #print i,j,"-",l,r
    i+=1
#for i in range(0,n+1):
  #for j in range(0,n+1):
    #print dp[i][j],
  #print  
print dp[1][n]	  
fout.write(str(dp[1][n]))
fout.close()
fin.close()