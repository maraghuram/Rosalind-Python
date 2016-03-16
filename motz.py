import timeit

fin=open("rosalind_motz.txt","r")
fout=open("rosalind_motz_ans.txt","w")
ferr=open("rosalind_motz_ans_complexity.txt","w")

s=''.join(fin.read().split("\n")[1:])
res=int(0)
mod=int(1000000)
dp=[]
n=len(s)
def solve():
    def comp(x):
        if x=="A":
            return "U"
        elif x=="U":
            return "A"
        elif x=="G":
            return "C"
        elif x=="C":
            return "G"
        
    global res,mod,s,dp,n        

    for i in range(0,n+1):
        l=[]
        for j in range(0,n+1):
            l.append(int(1))
        dp.append(list(l))
         
    for i in range(1,n):
        if s[i]==comp(s[i-1]):
            dp[i][i+1]=2            

    for sz in range(3,n+1):
        for i in range(1,n):
            j=i+sz-1
            if j<=n :
                dp[i][j]=dp[i+1][j]
                for k in range(i+1,j+1):
                    if s[k-1]==comp(s[i-1]):
                        dp[i][j]=(dp[i][j]+(dp[i+1][k-1]*(dp[k+1][j] if k+1<=j else 1))%mod)%mod    
    
t=timeit.Timer(solve)
ferr.write(str(t.timeit(1)))
fout.write(str(dp[1][n]))

fin.close()
fout.close()
ferr.close()
