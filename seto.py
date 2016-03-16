import timeit
fin=open("rosalind_seto.txt","r")
fout=open("rosalind_seto_ans.txt","w")
ferr=open("rosalind_seto_ans_complexity","w")

n=int(fin.readline())
U=set([x for x in range(1,n+1)])
l=fin.read()
first=l.split("}")[0]
second=l.split("}")[1]
first=first.replace("{","").replace(",","")
second=second.replace("{","").replace(",","")
A=set(map(int,first.split()))
B=set(map(int,second.split()))

aub=aib=adb=bda=uda=udb=set()

def solve():
    global aub,aib,adb,bda,uda,udb
    aub=A.union(B)
    aib=A.intersection(B)
    adb=A.difference(B)
    bda=B.difference(A)
    uda=U.difference(A)
    udb=U.difference(B)

t=timeit.Timer(solve)
ferr.write(str(t.timeit(1)))
fout.write(str(aub)+"\n")
fout.write(str(aib)+"\n")
fout.write(str(adb)+"\n")
fout.write(str(bda)+"\n")
fout.write(str(uda)+"\n")
fout.write(str(udb))

fin.close()
fout.close()
ferr.close()
