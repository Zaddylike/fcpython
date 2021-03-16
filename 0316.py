# data=[10,20,30,40,50]

# data.append(60)
# data.append("a")
# print(data)

# data.insert(1,"b")
# print(data)

# studenT=["john","peter","may","奶水"]
# while True:
#     quE=input("enter a name you enat to search")
#     if quE=="q":
#         break
#     if studenT.count(quE) != 0:
#         print(quE)
#     else:
#         namE=input("join a stuent in th list")
#         if namE.upper() == "Y":
#             studenT.append(quE)
# print("共有",studenT)


data=[100,1,3,70,60]
# data.sort(reverse=True)
# print(data)
# data.sort()
# print(data)
# n=sorted(data)
# print(n)
# n=sorted(data,reverse=True)
# print(n)

del data[0]
print(data)
del data[1:6:2]
print(data)