tup1=(1,2,3,4,5)
tup2=(6,7,8,9)
print("after adding two tuples")
tup3=tup1+tup2
print(tup3)
del tup3
print("successfull deleting tup3")
print("slicing of tuples")
print(tup1[:3])
print(tup1[1:-3])
print(tup1[-3:])
print(tup1[1:4])
tup3=tup1
print(tup3)
print("traverse tuple through loop")
for i in tup1:
    print(i)
list=[]
print("creating tuple user define")
for i in range(1,10):
    list.append(i)
print(tuple(list))
print(tuple)

