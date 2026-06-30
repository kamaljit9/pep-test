#q1
n=int(input("enter the size:"))
list1=[]
for i in range(n):
    x=int(input(""))
    list1.append(x)
def create_paginator():
    set1=set(list1)
    p=int(input("page size:"))
    list2=list(set1)
    for i in range(0,len(set1),p):
        x=list2[i:i+p]
        print(x)
create_paginator()
