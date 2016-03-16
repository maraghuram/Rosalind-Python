import timeit
import pickle
from itertools import permutations,combinations

fin=open("rosalind_rear.txt","r")
fout=open("rosalind_rear_ans.txt","w")
ferr=open("rosalind_rear_ans_complexity","w")

groups=fin.read().strip("\n").split("\n\n")
pairs=[]
for x in groups:
    pairs.append([tuple([int(y) for y in l.split()]) for l in x.split("\n")])
print (pairs)

def rev(p,x,y):    
    if x == 0:
        return p[y::-1] + p[y+1:]
    if y == len(p) - 1:
        return p[:x] + p[:x-1:-1]
    return p[:x] + p[y:x-1:-1] + p[y+1:]

def init_table(size=10):
    start=tuple(range(1,size+1))
    table={start:0}
    perms=set([x for x in permutations(range(1,size+1))])
    max_val=len(perms)
    old_set=set([start])
    new_set=set()
    while len(table) < max_val:
        print( len(table))
        for perm in old_set:
            depth=table[perm]
            for i,j in combinations(range(size),2):
                new_perm=rev(perm,i,j)
                if not new_perm in table:
                    new_set.add(new_perm)
                    table[new_perm]=depth+1
        old_set=new_set
        new_set=set()
        
    return table
   

try:
    with open('TABLE.pkl', 'rb') as ft:
        table = pickle.load(ft)
        print ("Table ready!")
except (IOError,pickle.UnpicklingError):
    table = init_table(10)
    with open('TABLE.pkl', 'wb') as ft:
        pickle.dump(table,ft)


def solve():
    global pairs
    for x,y in pairs:
        index_of_y=tuple([y.index(i+1)+1 for i in range(len(y))])
        index_of_y_wrt_x=tuple([index_of_y[xval-1] for xval in x])
        print(table[index_of_y_wrt_x])
        fout.write(str(table[index_of_y_wrt_x])+" ")
solve()

fin.close()
fout.close()
ferr.close()
