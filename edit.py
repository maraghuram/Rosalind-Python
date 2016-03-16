import timeit

fin=open("rosalind_edit.txt","r")
fout=open("rosalind_edit_ans.txt","w")
ferr=open("rosalind_edit_ans_complexity","w")

l=fin.read()
s=''.join(l.split(">")[1].split("\n")[1:])
t=''.join(l.split(">")[2].split("\n")[1:])
dp=[]
n=len(s)
m=len(t)

def solve():
    for i in range(0,n+1):
      l=[]
      for j in range(0,m+1):
	l.append(int(0))
      dp.append(l)

    for i in range(0,n+1):
      for j in range(0,m+1):
	if i==0 :
	  dp[i][j]=j
	elif j==0 :
	  dp[i][j]=i
	else:
	  dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+(0 if s[i-1]==t[j-1] else 1))

timer=timeit.Timer(solve)
ferr.write(str(timer.timeit(1)))
print dp[n][m]
fout.write(str(dp[n][m]))


fin.close()
ferr.close()
fout.close()
