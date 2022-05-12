dics={}

eop=True
bid=0
bname=""
while eop:
    name=input("Enter Your Name :")
    x=int(input("Enter Your Bid $"))
    dics[name]=x
    if bid<x:
        bid=x
        bname=name
    end=input("Do You Want To BId Again? yes or no :")
    if end != 'yes':
        eop=False
print(f"Winner is {bname}!!!")
print(dics)