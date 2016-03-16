fin=open("rosalind_lexf.txt","r")
fout=open("rosalind_lexf_ans.txt","w")
line=fin.readline().strip("\n")
n=int(fin.readline().strip("\n"))

symbols=line.split(" ")
string=[]

def rec(sz):
  if sz==n:
    fout.write(str(string).strip("]").strip("[").replace(", ","").replace("'","")+"\n")
    return
  for i in range(0,len(symbols)):
    string.append(symbols[i])
    rec(sz+1)
    string.pop()

rec(0)

fin.close()
fout.close()    

