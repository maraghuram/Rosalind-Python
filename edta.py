import timeit

fin=open("rosalind_edta.txt","r")
fout=open("rosalind_edta_ans.txt","w")
ferr=open("rosalind_edta_ans_complexity.txt","w")

l=fin.read()
s=''.join(l.split(">")[1].split("\n")[1:])
t=''.join(l.split(">")[2].split("\n")[1:])
m=len(s)+1
n=len(t)+1

def solve():
  dp=[]
  back=[]
  for i in range(m):
    x=[]
    b=[]
    for j in range(n):
      x.append(0)
      b.append(-1)
    dp.append(list(x))
    back.append(list(b))
    
  for i in range(1,m):
    dp[i][0]=i
    back[i][0]=1
  for j in range(1,n):
    dp[0][j]=j
    back[0][j]=2
  for i in range(1,m):
    for j in range(1,n):
      dp[i][j]=min(dp[i-1][j-1]+(0 if s[i-1]==t[j-1] else 1),min(dp[i-1][j]+1,dp[i][j-1]+1))
      if dp[i][j]== (dp[i-1][j-1]+(0 if s[i-1]==t[j-1] else 1)):
	back[i][j]=0
      elif dp[i][j]==dp[i-1][j]+1:
	back[i][j]=1
      else:
	back[i][j]=2	

  s1,t1="",""
  i,j=m-1,n-1
  while not back[i][j]==-1:
    if back[i][j]==0:
      s1+=s[i-1]
      t1+=t[j-1]
      i-=1
      j-=1
    elif back[i][j]==1:
      t1+="-"
      s1+=s[i-1]
      i-=1
    else:
      s1+="-"
      t1+=t[j-1]
      j-=1

  print s1[::-1],t1[::-1]
  print dp[m-1][n-1]

  fout.write(str(dp[m-1][n-1])+"\n"+s1[::-1]+"\n"+t1[::-1])


timer=timeit.Timer(solve)
ferr.write(str(timer.timeit(1)))  

fin.close()
fout.close()
ferr.close()
