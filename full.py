import timeit

fin=open("rosalind_full.txt","r")
fout=open("rosalind_full_ans.txt","w")
ferr=open("rosalind_full_ans_complexity.txt","w")

weight = {71.03711: 'A', 103.00919: 'C', 115.02694: 'D', 129.04259: 'E',
147.06841: 'F', 57.02146: 'G', 137.05891: 'H', 113.08406: 'I', 128.09496: 'K',
113.08406: 'L', 131.04049: 'M', 114.04293: 'N', 97.05276: 'P', 128.05858: 'Q',
156.10111: 'R', 87.03203: 'S', 101.04768: 'T', 99.06841: 'V', 186.07931: 'W',
163.06333: 'Y'}


def solve():
  parent_mass=float(fin.readline())
  ions=[float(x) for x in fin.readlines()]
  pairs=[]
  index=0
  while (index<len(ions)/2):
    min_ion=0
    min_distance=400
    for ion in ions:
      if abs(parent_mass - ions[index] - ion)<min_distance:
	min_ion=ion
	min_distance=abs(parent_mass - ions[index] - ion)
    pairs.append((ions[index], min_ion))
    index+=1
  i=0
  result=""
  
  while i<len(ions)/2-1:
    near = None
    tol = 1
    for candidate in weight.keys():
      if round(abs(pairs[i+1][0] - pairs[i][0]- candidate), 3) == 0:
	tol = abs(pairs[i+1][0] - pairs[i][0]- candidate)
	near = candidate
    if not near:
      pairs[i+1] = (pairs[i+1][1], pairs[i+1][0])
      pairs.sort()
      i=0
      result=""
    else:
      result+=str(weight[near])
      i+=1
  fout.write(result)
  

timer=timeit.Timer(solve)        

ferr.write(str(timer.timeit(1)))

fin.close()
fout.close()
ferr.close()


