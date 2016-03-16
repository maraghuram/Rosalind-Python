fin=open("rosalind_iev.txt","r")
fout=open("rosalind_iev_ans.txt","w")

x1,x2,x3,x4,x5,x6= fin.read().strip("\n").split(" ")
res=float(0.0)
res=(int(x1)*2.0)+(int(x2)*2.0)+(int(x3)*2.0)+(int(x4)*1.50)+(int(x5)*1.0)
fout.write(str("%.1f" %res))