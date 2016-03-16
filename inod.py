fin=open("rosalind_inod.txt","r")
fout=open("rosalind_inod_ans.txt","w")
n=int(fin.read())
print n-2
fout.write(str(n-2))
fin.close()
fout.close()