fin=open("rosalind_subs.txt","r")
fout=open("rosalind_subs_ans.txt","w")
lines=fin.readlines()
s=lines[0].strip("\n")
t=lines[1].strip("\n")

start=0
while True:
	start=s.find(t,start)
	if start==-1 :
		break
	fout.write(str(start+1)+" ")
	start+=1
	


