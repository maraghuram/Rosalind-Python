fin=open("rosalind_prot.txt","r")
fout=open("rosalind_prot_ans.txt","w")
cod=open("codon_table.txt","r")
lookup=dict()
for line in cod.readlines():
    line=line.strip("\n")
    i=int(0)
    pairs=line.split(" ")    
    for i in range(0,int(len(pairs)/2)):        
        lookup[pairs[2*i]]=pairs[2*i+1]    

s=fin.read().strip("\n")
output=""
i=int(0)
for i in range(0,int(len(s)/3)):
    x=lookup[""+s[3*i]+s[3*i+1]+s[3*i+2]]
    if x=="Stop":
        break
    else:
        output=output+x
        
fout.write(output+"\n")