n = int(input("Enter number of products: "))
name = []
price = []
weight = []
print("Enter names:")
for i in range(n):
    name.append(input())
print("Enter prices:")
for i in range(n):
    price.append(int(input()))
print("Enter weights:")
for i in range(n):
    weight.append(int(input()))
s=set()
count=0
for i in range(n):
    product = (name[i], price[i], weight[i])
    if product in s:
        count += 1
    else:
        s.add(product)
print(count)
