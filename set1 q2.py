q2
n=int(input("size:"))
arr=[]
for i in range(n):
    x=int(input(""))
    arr.append(x)
m=int(input("operations size: "))
mcol=2
mlist=[]
list1=[]
for i in range(m):
    list1=[]
    for j in range(mcol):
        p=int(input(""))
        list1.append(p)
    mlist.append(list1)
for i in range(m):
    s=mlist[i][0]
    e=mlist[i][1]
    arr[s:e+1]=arr[s:e+1][::-1]
print(arr)