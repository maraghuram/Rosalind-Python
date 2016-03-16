import timeit
fin=open("rosalind_lrep.txt","r")
fout=open("rosalind_lrep_ans.txt","w")
ferr=open("rosalind_lrep_ans_complexity.txt","w")

s=fin.readline().strip()
k=int(fin.readline().strip())
edges=[edge.strip() for edge in fin.readlines()]
graph=dict()
nodes=[]

def dfs(node,par,curr):
  its=int(0)
  for adj in graph[node]:
    x,y=adj
    if not x==par:
      its+=dfs(x,node,curr+y)
  nodes.append((node,curr,its))
  
  return 1 if its==0 else its
    
def solve(): 

  for edge in edges:
    u,v,x,y = edge.split(" ")
    x=int(x)-1
    y=int(y)
    if not u in graph:
      graph[u]=[(v,s[x:x+y])]
    else:
      graph[u].append((v,s[x:x+y]))
    if not v in graph:
      graph[v]=[(u,s[x:x+y])]
    else:
      graph[v].append((x,s[x:x+y]))
      
  #print graph
  dfs("node1",None,"")
  #print nodes
  best=""
  for node in nodes:
    x,y,z=node
    if z>=k:
      if len(y)> len(best):
	best=y
  print best
  fout.write(best)

timer=timeit.Timer(solve)
ferr.write(str(timer.timeit(1)))

fin.close()
fout.close()
ferr.close()
