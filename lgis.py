fin=open("rosalind_lgis.txt","r")
fout=open("rosalind_lgis_ans.txt","w")
n=int(fin.readline())
perm=fin.readline().strip("\n").split(" ")
for i in range(0,n):
  perm[i]=int(perm[i])


lis=[1]*(n+1)
back=[-1]*(n+1)

for i in range(0,n):
  for j in range(0,i):
    if perm[i] > perm[j] and lis[i] < lis[j]+1 :
      lis[i]=lis[j]+1
      back[i]=j
      
bestIndex=0
best=lis[0]
for i in range(1,n):
 if lis[i]>best:
   best=lis[i]
   bestIndex=i
res=[]
curr=bestIndex   
while not curr==-1:
  res.append(perm[curr])
  curr=back[curr]
print res[::-1]
fout.write(str(res[::-1]).strip("[").strip("]").replace("'","").replace(","," ")+"\n")
print len(res)
lds=[1]*(n+1)
back=[-1]*(n+1)

for i in range(0,n):
  for j in range(0,i):
    if perm[j] > perm[i] and lds[i] < lds[j]+1 :
      lds[i]=lds[j]+1
      back[i]=j
            
bestIndex=0
best=lds[0]
for i in range(1,n):
  if lds[i]>best:
    best=lds[i]
    bestIndex=i
res=[]
curr=bestIndex
while not curr==-1:
  res.append(perm[curr])
  curr=back[curr]
print res[::-1]
fout.write(str(res[::-1]).strip("[").strip("]").replace("'","").replace(","," ")+"\n")

fin.close()
fout.close()