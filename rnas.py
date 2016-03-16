import timeit

def valid(x):
    if x=="A":
        return ("U")
    if x=="U":
        return ("A","G")
    if x=="C":
        return ("G")
    if x=="G":
        return ("C","U")


fin=open("rosalind_rnas.txt","r")
fout=open("rosalind_rnas_ans.txt","w")
ferr=open("rosalind_rnas_ans_complexity.txt","w")

s=fin.read().strip()
n=len(s)
dp=[]

def solve():
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(int(0))
        dp.append(list(l))

    for sz in range(1,n+1):
        for i in range(n-sz+1):
            j=i+sz-1
            if sz<=4:
                dp[i][j]=1
            else:
                dp[i][j]+= dp[i+1][j]
                for k in range(i+4,j+1):
                    if s[k] in valid(s[i]):
                        dp[i][j]+=(dp[i+1][k-1]*(dp[k+1][j] if k+1<=j else 1))
    print dp[0][n-1]
    fout.write(str(dp[0][n-1]))
    
timer=timeit.Timer(solve)
ferr.write(str(timer.timeit(1)))
    
fin.close()
fout.close()
ferr.close()
