fin=open("rosalind_prtm.txt","r")
fout=open("rosalind_prtm_ans.txt","w")
mass=open("mass_table.txt","r")
table=dict()
for line in mass.readlines():
  key,val=line.split()
  table[key]=val

string=fin.read().strip("\n");
res=0.0
for c in string:
  res+=float(table[c])
fout.write("%.3f" % res)

fin.close()
fout.close()
mass.close()
  