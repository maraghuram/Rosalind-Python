fin=open("rosalind_revp.txt","r")
fout=open("rosalind_revp_ans.txt","w")

string=""
flag=False
for line in fin.readlines():
  if not flag:
    flag=True
    continue
  line=line.strip("\n")
  string+=line

def complement(x,y):
  if x=="A" and y=="T":
    return True
  if x=="T" and y=="A":
    return True
  if x=="G" and y=="C":
    return True
  if x=="C" and y=="G":
    return True
  return False  
    
def isPalindrome(x):
  size=len(x)
  left=x[0:size/2]
  right=x[:((size+1)/2)-1:-1]
  #print left+" "+right
  flag=True  
  for j in range(0,size/2):
   # print left[i],right[-(i+1)]
    if not complement(left[j],right[j]):
      flag=False
  return flag

mx=len(string)  
for i in range(0,mx):  
  for sz in range(4,13):
    if sz%2==0 and i+sz<=mx:
      substr=string[i:i+sz]    
      if isPalindrome(substr):	
	print i+1,sz
	fout.write(str(i+1)+" "+str(sz)+"\n")
    
fin.close()
fout.close()  
