import timeit
fin=open("rosalind_spec.txt","r")
fout=open("rosalind_spec_ans.txt","w")
ferr=open("rosalind_spec_ans_complexity.txt","w")

spec=[float(i) for i in fin.read().strip().split('\n')]
string=""

mass = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}
alpha=list(mass.keys())
def solve():
    global string
    global spec
    diffspec=[spec[i+1]-spec[i] for i in range(len(spec)-1)]    
    for var in diffspec:
        mindiff=float("inf")
        index=-1
        pos=int(0)
        for a,b in mass.items():
            if abs(b-var) < mindiff:
                index=pos
                mindiff=abs(b-var)
            pos+=1                 
        string+=alpha[index]
        
t=timeit.Timer(solve)
ferr.write(str(t.timeit(1)))
fout.write(string)

fin.close()
fout.close()
ferr.close()
