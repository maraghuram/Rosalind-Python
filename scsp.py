import timeit

fin=open("rosalind_scsp.txt","r")
fout=open("rosalind_scsp_ans.txt","w")
ferr=open("rosalind_scsp_ans_complexity.txt","w")

s=fin.readline().strip("\n")
t=fin.readline().strip("\n")
m=len(s)+1
n=len(t)+1
print (s)
print (t)
lcs=""
scsp=""

def getLcs():
    global lcs
    res=[]
    prev=[]
    for i in range(0,m):
        l=[]
        for j in range(0,n):
            l.append(int(0))            
        res.append(list(l))
        prev.append(list(l))
    for i in range(0,m):
        res[i][0]=0
        prev[i][0]=1
    for j in range(0,n):
        res[0][j]=0
        prev[0][j]=0
        
    for i in range(1,m):
        for j in range(1,n):
            if i ==0 or j==0:
                res[i][j]=0 
            elif s[i-1]==t[j-1] :     
                res[i][j]=res[i-1][j-1]+1
                prev[i][j]=2        
            else:
                res[i][j]=max(res[i-1][j],res[i][j-1])
                if res[i][j]==res[i-1][j]:
                    prev[i][j]=1

    i,j=m-1,n-1
    lcs=""
    
    while i !=0 or j !=0:
        print( i,j)
        if prev[i][j]==2:
            lcs+=s[i-1]
            i=i-1
            j=j-1
        elif prev[i][j]==1:
            i=i-1
        else:
            j=j-1

    lcs=lcs[::-1]

def solve():
    global scsp,s,t,lcs
    i=j=0
    getLcs()
    for x in lcs:
        if i <len(s):
           while not s[i]==x:
               scsp+=s[i]
               i+=1
           i+=1
        if j <len(t):
            while not t[j]==x:
                scsp+=t[j]
                j+=1
            j+=1
        scsp+=x
    if i<len(s):
        scsp+=s[i:]
    if j<len(t):
        scsp+=t[j:]

timer=timeit.Timer(solve)
ferr.write(str(timer.timeit(1)))
fout.write(scsp)
print (scsp)


fin.close()
fout.close()
ferr.close()
