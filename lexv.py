import timeit
fin=open("rosalind_lexv.txt","r");
fout=open("rosalind_lexv_ans.txt","w");
ferr=open("rosalind_lexv_info.txt","w");
l=fin.read().split("\n")
alphabet=l[0].split(" ")
print(alphabet)
max_depth=int(l[1])
def solve_helper():
    def solve(string,depth):
        if depth>max_depth:
            return
        if len(string)!=0 :
            #print(str(string).replace(",","").replace("[","").replace("]","").replace("'",""))
            fout.write( str(string).replace(",","").replace("[","").replace("]","").replace("'","").replace(" ","") +"\n" )
        for alpha in alphabet :
            string.append(alpha)
            solve(string,depth+1)
            string.pop()
    solve([],0)
    
time=timeit.Timer(solve_helper)
ferr.write( " Alphabet size (m) = "+str(len(alphabet))+"\n" +
            " Input size (n) = "+str(max_depth)+"\n" )
ferr.write( " Execution time of Solve() = " +str(time.timeit(1))+" s" )
ferr.write( "\n Time Complexity : O(mn) \n Space Complexity : O(mn) "+
            "  where 'm' is the length of the first input string and "+
            "\n 'n' is the length of the Second input string.")
ferr.close();
#fout.write(lcs)
fin.close();
fout.close();




