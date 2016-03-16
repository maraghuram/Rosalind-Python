fd=open("rosalind_fib.txt","r")
l=fd.readlines()[0].strip("\n").split(" ")
n=int(l[0])
k=int(l[1])
mem=[int(-1)]*50
mem[0]=int(0)
mem[1]=int(1)
for i in range(2,n+1):
	mem[i]=mem[i-1]+(k*mem[i-2])
print mem[n]
