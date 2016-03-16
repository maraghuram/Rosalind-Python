fin=open("rosalind_long.txt","r")
fout=open("rosalind_long_ans.txt","w")
graph=[]
nodes=[]
def compare(x,y):
  for i in range(len(x)):
    looking_for = x[i:]
    if (y[:len(looking_for)] == looking_for):
      return len(looking_for)
    
  return 0

class DFS:
  
  def __init__(self, nodes,edges):
    self.nodes = nodes
    self.edges = edges
    self.paths=[]
    self.visited=[]

  def dfs_visit(self,node,path,end):    
    if node==end:      
      if len(path)==len(self.nodes):
	self.paths.append(list(path))
      return
    for x in graph[node]:
      if not self.visited[x]:
	self.visited[x]=True
	path.append(x)
	self.dfs_visit(x,path,end)
	path.pop()
	self.visited[x]=False
    return							  
    
  def dfs_helper(self,start,end):
    self.visited=[False]*len(nodes)    
    self.visited[start]=True
    self.dfs_visit(start,[start],end)    
    return self.paths

curr=""
for line in fin.readlines():
  if line[0]==">":
    if not curr=="":
      nodes.append(curr)
    curr=""
  else:
    curr+=line.strip("\n")
nodes.append(curr)
print nodes

sz=len(nodes)
for i in range(sz):
  adj=[]
  for j in range(sz):
    if not i==j:
      overlap = compare(nodes[i],nodes[j])
      if overlap >= len(nodes[j])/2:
	adj.append(j)
  graph.append(adj)
  
print graph
dfs=DFS(nodes,graph)
for i in range(sz):
  for j in range(sz):
    if not i==j:
      dfs.dfs_helper(i,j)
      
superstring=""
currstring=""
for path in dfs.paths:
  print path
  currstring=nodes[path[0]]
  for i  in range(1,sz):
    overlap=compare(nodes[path[i-1]],nodes[path[i]])
    currstring+=nodes[path[i]][overlap:]    
  if len(currstring) < len(superstring) or superstring=="":
    superstring=currstring    

print superstring
fout.write(superstring)
fin.close()
fout.close()     
      
      
      
  
    