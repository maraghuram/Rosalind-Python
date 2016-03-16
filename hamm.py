fin=open("rosalind_hamm.txt","r")
fout=open("rosalind_hamm_ans.txt","w")
lines=fin.readlines()
s=lines[0].strip("\n")
t=lines[1].strip("\n")
count=int(0)

for i in range(0,len(s)):
    if s[i]!=t[i]:
        count=count+1
fout.write(str(count))  
