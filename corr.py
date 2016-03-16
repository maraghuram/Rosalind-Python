fin=open("rosalind_corr.txt","r")
fout=open("rosalind_corr_ans.txt","w")
curr=""
strings=[]
fixed=[]
for line in fin.readlines():
    if line[0]==">":
        if not curr=="":
            strings.append(curr)
            curr=""
    else:
        curr=curr+line.strip("\n")
        
if not curr=="":
    strings.append(curr)
    curr=""

def comp(x):
    res=""
    for i in range(len(x)-1,-1,-1):
        if x[i]=="A":
            res+="T"
        elif x[i]=="T":
            res+="A"
        elif x[i]=="G":
            res+="C"
        else:
            res+="G"
    return res

for i in range(0,len(strings)):
    for j in range(0,len(strings)):
        if not i==j:
            if strings[j]==strings[i] or strings[j]==comp(strings[i]):
                fixed.append(strings[i])
                fixed.append(comp(strings[i]))

errors=[]                
for var in strings:
    if not var in fixed:
        errors.append(var)        

def calc(x,y):
    res=0
    for i in range(0,len(x)):
        if not x[i]==y[i]:
            res+=1
    return res       
        
for err in errors:
    for var in fixed:
        dist=calc(err,var)
        if dist<=1 :
            print err,var
            fout.write(err+"->"+var+"\n")
            break

fin.close()
fout.close()