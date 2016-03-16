import timeit
fin=open("rosalind_kmp.txt","r");
fout=open("rosalind_kmp_ans.txt","w");
ferr=open("rosalind_kmp_ans_complexity.txt","w");
s=''.join(fin.read().split("\n")[1:])
res=[int(0)]*(len(s)+1)
res[0]=-1
def solve():
    k=2
    cnd=0
    while k < len(s):
        if s[k-1] == s[cnd]:
            cnd += 1
            res[k] = cnd
            k += 1
        elif cnd > 0:
            cnd = res[cnd]
        else:
            res[k] = 0
            k += 1
t=timeit.Timer(solve)
ferr.write( " Input size (n) = "+str(len(s))+"\n" )
ferr.write( " Execution time of Solve() = " +str(t.timeit(1))+" s" )
ferr.write( "\n Time Complexity : O(n) \n Space Complexity : O(n) "+
            "  where 'n' is the length of the input string " )
ferr.close();
#print( ' '.join([str(i) for i in res[1:]]) )
fout.write(' '.join([str(i) for i in res[1:]]))
fin.close();
fout.close();




