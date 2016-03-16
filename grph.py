fin=open("rosalind_grph.txt","r")
fout=open("rosalind_grph_ans.txt","w")

lines=fin.readlines()
currstr=""
ids=list()
strings=list()

for line in lines:
    line=line.strip("\n").strip(" ")
    if line[0]==">":
        if not currstr=="":
            strings.append(currstr)
        currstr=""
        ids.append(line.strip(">"))
    else:
        currstr+=line
if not currstr=="":
    strings.append(currstr)
    
def match(a,b):
    if a[-3]==b[0] and a[-2]==b[1] and a[-1]==b[2]:
        return True
    else:
        return False
first=True    
sz=len(strings)    
for i in range(0,sz):
    for j in range(0,sz):
        if not i==j:
            if match(strings[i],strings[j]):
                if first:
                    fout.write(ids[i]+" "+ids[j])
                    first=False
                else:        
                    fout.write("\n"+ids[i]+" "+ids[j])
            