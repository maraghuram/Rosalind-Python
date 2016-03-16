import urllib2

fin=open("rosalind_mprt.txt","r")
fout=open("rosalind_mprt_ans.txt","w")

for prot in fin.readlines():
    prot=prot.strip("\n")
    target_url="http://www.uniprot.org/uniprot/"+prot+".fasta"
    data = urllib2.urlopen(target_url)
    pos=[]
    flag=False
    string=""
    for line in data:
        line=line.strip("\n")
        if not flag:
            flag=True
            continue
        else:
            string+=line            

    string.strip("\n").strip(" ")
    flag=False   
    print string
    for i in range(0,len(string)):
        if string[i]=="N" and i<len(string)-3:
            if not string[i+1]=="P":
                if string[i+2]=="S" or string[i+2]=="T":
                    if not string[i+3]=="P":
                        flag=True
                        pos.append(i+1)
    if flag:
        fout.write(prot+"\n"+str(pos).replace(","," ").strip("[").strip("]")+"\n")
        
fout.close()
fin.close()
