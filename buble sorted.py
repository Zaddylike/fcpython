data=[10,20,90,5,1,7]
n=len(data)
for i in range(n-1): # 掃描一趟的總次數
    for j in range(n-i-1): #每一趟掃描交換的次數
        if data[j]>data[j+1]:
            data[j],data[j+1]=data[j+1],data[j]
print(data)