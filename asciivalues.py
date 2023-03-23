#print ascii values of the string

print("ASCII as values and characters as keys")
yy={}
print("enter the string")
a=input()
b=[]
for i in range(256):
    ch = chr(i)
    yy.update({ch:i})
print(yy)
for j in a:
    x=yy[j]
    b.append(x)
print(b)