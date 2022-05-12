raw1=["😁","😁","😁"]
raw2=["😁","😁","😁"]
raw3=["😁","😁","😁"]
map=[raw1,raw2,raw3]
print(f"{raw1}\n{raw2}\n{raw3}")
position=input("Enter Position Where you want treasure :")
rawpos=int(position[1])-1
colpos=int(position[0])-1
map[rawpos][colpos]='X'
print(f"{raw1}\n{raw2}\n{raw3}")
