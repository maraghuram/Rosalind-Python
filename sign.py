from itertools import permutations

fin=open("rosalind_sign.txt","r")
fout=open("rosalind_sign_ans.txt","w")

n=int(fin.read())
l=[]
for i in range(1,n+1):
  l.append(i)
  l.append(-i)
  
combs=list(permutations(l,n))
res=[]

for comb in combs:
  x=list(comb)
  done=[False]*(n+1)
  flag=True  
  for var in x:
    if done[abs(var)]:
      flag=False
      break
    done[abs(var)]=True  
  if flag:
    res.append(comb)
    
print len(res)
fout.write(str(len(res))+"\n")
for comb in res:
  print comb
  fout.write(str(comb).strip(")").strip("(").replace(",","")+"\n")
  
fin.close()
fout.close()  