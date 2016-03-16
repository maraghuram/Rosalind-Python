def nC2(n):
    return float((n))*(n-1)/2

fin=open("rosalind_iprb.txt","r")
fout=open("rosalind_iprb_ans.txt","w")
line=fin.read()
line=list(line.split(" "))
k=int(line[0])
m=int(line[1])
n=int(line[2])

tot=int(k+m+n)
dom=float(0.0)

for i in range(0,k):
   dom=dom+(tot-i-1)
dom=dom+(nC2(m)*0.75)+((nC2(m+n)-nC2(m)-nC2(n))*0.5)
dom=dom/(nC2(tot))
fout.write(str("%.5f" %dom))