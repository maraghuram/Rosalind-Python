import timeit

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

fin=open("rosalind_trie.txt","r")
fout=open("rosalind_trie_ans.txt","w")
ferr=open("rosalind_trie_ans_complexity.txt","w")

strings=[]
for line in fin.readlines():
		strings.append(line.strip("\n"))
ctr=1

class Node:	
	def __init__(self):
		self.links=[None]*len(alphabet)
	def checkNode(self,x):
		return (self.links[alphabet.find(x)]==None)
	def addNode(self,x):				
		self.links[alphabet.find(x)]=Node()		
	def getNode(self,x):
		return self.links[alphabet.find(x)]
		
def dfs(node):	
	global ctr
	temp=ctr	
	for a in alphabet:
		if not node.checkNode(a):
			ctr+=1
			print temp, ctr, a		
			fout.write(str(temp)+" "+str(ctr)+" "+str(a)+"\n")
			dfs(node.getNode(a))
			

def solve():	
	global strings
	root=Node()
	for line in strings:
		ptr=root		
		for c in line:
			if ptr.checkNode(c):
				ptr.addNode(c)				
			ptr=ptr.getNode(c)			
	dfs(root)	
		
	 

timer=timeit.Timer(solve)		
ferr.write(str(timer.timeit(1)))

fin.close()
fout.close()
ferr.close()
