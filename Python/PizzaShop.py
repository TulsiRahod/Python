size=input("Enter size for Pizza S | M | L :")
peper=input("would you like to have pepperoni? Y | N :")
cheez=input("would you like to have extra cheez? Y | N :")
bill=0
if size=='s':
    bill+=15
elif size=='m':
    bill+=20
elif size=='l':
    bill+=25
else:
    print("Enter Valid Choice")

if peper=='y':
    if size=='s':
        bill+=2
    else:
        bill+=3

if cheez=='y':
    bill+=1
print(f"Total Bill is {bill}$")