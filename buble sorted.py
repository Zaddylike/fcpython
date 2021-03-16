data=[10,20,90,5,1,7]
n=len(data)
for i in range(n-1):
    for j in range(n-i-1):
        if data[j]>data[j+1]:
            data[j],data[j+1]=data[j+1],data[j]
print(data)