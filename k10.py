l1=[1,2,3,4]
l2=[5,6,3,4]
l=[]
for i in l1:
    if i in l2:
        l.append(i)
for i in l:
    l1.remove(i)
    l2.remove(i)
print(l1,l2)