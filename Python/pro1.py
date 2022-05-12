a=input()
a=a.split(" ")
print(len(a))
for x in range(len(a)):
    length=len(a[x])
    b=a[x]
    s=b[0]
    for y in range(1,length):
        if b[y]>b[y-1]:
            u=b[y].upper()
            s+=u
        else:
            l=b[y].lower()
            s+=l
    a[x]=s
    print(a[x])
print(a)
mystring=" ".join(a)
print(mystring)




