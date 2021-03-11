nuM=int(input("enter a nuM: "))
for i in range(0,nuM):
    for x in range(0,nuM-i):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
for ii in range(0,nuM+1):
    for xx in range(0,ii):
        print(" ",end="")
    for jj in range(2*nuM-(2*ii-1)):
        print("*",end="")
    print()
