import timeit
fin=open("rosalind_lcsq.txt","r");
fout=open("rosalind_lcsq_ans.txt","w");
ferr=open("rosalind_lcsq_ans_complexity.txt","w");
l=fin.read().split(">")
s=''.join(l[1].split("\n")[1:])
t=''.join(l[2].split("\n")[1:])
print(s,t)
m=len(s)+1
n=len(t)+1

lcs=""

def solve():
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
        for j in range(0,n):
            if i ==0 or j==0 :
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
        if prev[i][j]==2:
            lcs+=s[i-1]
            i=i-1
            j=j-1
        elif prev[i][j]==1:
            i=i-1
        else:
            j=j-1

    lcs=lcs[::-1]            
        
time=timeit.Timer(solve)
solve()                
print(lcs)
ferr.write( " Input size (m) = "+str(len(s))+"\n" +
            " Input size (n) = "+str(len(t))+"\n" )
ferr.write( " Execution time of Solve() = " +str(time.timeit(1))+" s" )
ferr.write( "\n Time Complexity : O(mn) \n Space Complexity : O(mn) "+
            "  where 'm' is the length of the first input string and "+
            "\n 'n' is the length of the Second input string.")
ferr.close();
fout.write(lcs)
fin.close();
fout.close();
ferr.close();



