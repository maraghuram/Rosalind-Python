fd=open("rosalind_ini3.txt","r")
lines=fd.readlines()
string=lines[0].strip("\n")
limits=lines[1].strip("\n")
numbers=limits.split(" ")
a=int(numbers[0])
b=int(numbers[1])
c=int(numbers[2])
d=int(numbers[3])
print string[a:b+1],string[c:d+1]


