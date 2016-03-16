#!/usr/bin/env python


f=open("rosalind_gc.txt","r");
lines=f.readlines()
currentFasta=bestFasta=""
bestGC=float("-inf")
currentGC=float(0.0);
count=int(0)
for line in lines:
    if line[0]==">" and count!=0:
        currentGC=(currentGC*100)/float(count)
        if currentGC>bestGC:
             bestFasta=currentFasta       
             bestGC=currentGC
        currentFasta=line
        currentGC=float(0.0)
        count=int(0)
    else:
        for c in line:
            if c=="G" or c=="C":
                currentGC=currentGC+1
                count=count+1
            elif c=="A" or c=="T":
                count=count+1

currentGC=(currentGC*100)/float(count)
if currentGC>bestGC:
    bestFasta=currentFasta       
    bestGC=currentGC

print (bestFasta.strip(">").strip("\n"))
print ("%.6f" % bestGC)