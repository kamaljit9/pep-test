#q1
# n=int(input("enter the size:"))
# list1=[]
# for i in range(n):
#     x=int(input(""))
#     list1.append(x)
# set1=set(list1)
# p=int(input("page size:"))
# list2=list(set1)
# for i in range(0,len(set1),p):
#     x=list2[i:i+p]
#     print(x)

#q2
# n=int(input("size:"))
# arr=[]
# for i in range(n):
#     x=int(input(""))
#     arr.append(x)
# m=int(input("operations size: "))
# mcol=2
# mlist=[]
# list1=[]
# for i in range(m):
#     list1=[]
#     for j in range(mcol):
#         p=int(input(""))
#         list1.append(p)
#     mlist.append(list1)
# for i in range(m):
#     s=mlist[i][0]
#     e=mlist[i][1]
#     arr[s:e+1]=arr[s:e+1][::-1]
# print(arr)

#test3
#q1
def t(text):
    for i in text:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for i in dict:
        if dict[i]>=k:
            li.append(i)
    return li
        
text=input("enter the text:")
text=text.split(" ")
dict={}
k=int(input("Enter the k: "))
li=[]
print(t(text))
