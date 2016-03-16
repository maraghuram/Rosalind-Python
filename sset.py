import timeit
fin=open("rosalind_sset.txt","r");
fout=open("rosalind_sset_ans.txt","w");
ferr=open("rosalind_sset_ans_complexity.txt","w")

n=int(fin.read())
res=int(1)
def solve():
  global res
  MOD=int(1000000)
  i=n
  def power(x,y):
    if y==0:
      return 1
    elif y==1:
      return x
    elif y%2==0:
      return (power(x,y/2)*power(x,y/2))%MOD
    else:
      return (x*power(x,y-1))%MOD
    
  res=power(2,n)
  
t=timeit.Timer(solve)
ferr.write(str(t.timeit(1)))
fout.write(str(res))
print res

fout.close()
ferr.close()
fin.close()