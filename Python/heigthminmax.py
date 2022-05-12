height=input("Enter Students Heights :").split()

max=0
for x in height:
    if max<int(x):
        max=int(x)
print(f"Highest Height is {max} CM")

min=999
for y in height:
    if min>int(y):
        min=int(y)
print(f"Lowest Height is {min} CM")