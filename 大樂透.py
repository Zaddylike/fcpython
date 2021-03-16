import random

nuM=[]
while len(nuM) !=6:
    n=random.randint(1,49)
    if nuM.count(n) == 0:
        nuM.append(n)
print(nuM)