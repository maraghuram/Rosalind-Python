import timeit
comp={'A':'T','T':'A','G':'C','C':'G'}


def reverse(x):
  y=""
  for i in range(len(x)):
    y+=comp[x[i]]
  return y[::-1]
  

fin=open("rosalind_dbru.txt","r")
fout=open("rosalind_dbru_ans.txt","w")
ferr=open("rosalind_dbru_ans_complexity.txt","w")

strings=fin.read().strip().split("\n")
edges=set()

def solve():
  global edges
  rev = [reverse(s) for s in strings]
  strings.extend(rev)
  edges = set([(s[:-1], s[1:]) for s in strings])
  
timer=timeit.Timer(solve)
ferr.write(str(timer.timeit(1)))
for edge in edges:
  fout.write("("+edge[0]+","+edge[1]+")\n")
	
fin.close()
fout.close()
ferr.close()
