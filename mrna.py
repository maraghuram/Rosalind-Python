fin=open("rosalind_mrna.txt","r")
fout=open("rosalind_mrna_ans.txt","w")
codon=open("reverse_codon_table.txt","r")
table=dict()
mod=int(1000000)
res=int(1)

for line in  codon.readlines():
    line.strip("\n")
    key=line.split(" ")[0]
    val=line.split(" ")[1]    
    table[key]=val
    
data=fin.read().strip("\n")

for c in data:
    res=(res*int(table[c]))%mod
res=(res*3)%mod    
print res    
fout.write(str(res))
fin.close()
fout.close()
        
