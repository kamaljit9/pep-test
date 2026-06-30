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
