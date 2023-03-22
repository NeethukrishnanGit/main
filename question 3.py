l = [1, 2, 3, 5, 11, 2, 2, 444, 2321]
k = []
for i in range(len(l)):
    if l[i] < 10:
        k.append(l[i])
print(k)
