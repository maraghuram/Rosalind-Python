fin=open("rosalind_tree.txt","r")
fout=open("rosalind_tree_ans.txt","w")
n=int(fin.readline())
graph={}
components=0
visited=[False]*(n+1)
for i in range(1,n+1):
    graph[i]=[]
for line in fin.readlines():
    u,v = line.split(" ")
    u=int(u)
    v=int(v)
    graph[u].append(v)    
    graph[v].append(u)

def dfs(node):
    for adj in graph[node]:
        if not visited[adj]:
            visited[adj]=True
            dfs(adj)

for node in range(1,n+1):
    if not visited[node]:
        dfs(node)
        components+=1
print components-1
fout.write(str(components-1))

fin.close()
fout.close()