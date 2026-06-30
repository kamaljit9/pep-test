#q2
n = int(input("Enter number of bags: "))
weights = []
for i in range(n):
    x=float(input("Weight: "))
    weights.append(x)
weights.sort()
i = 0
j = n-1
count= 0
while i<=j:
    if i==j:
        count+= 1
        break
    if weights[i]+weights[j]<=3.0:
        i += 1
        j -= 1
    else:
        j -= 1
    count += 1
print(count)