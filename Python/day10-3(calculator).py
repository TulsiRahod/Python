def add(x,y):
    return x+y
def dif(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

def cal():
    eop=True
    while eop:
        no1=float(input("Enter First operand :"))
        ex=input("Enter Opration + - * / :")
        no2=float(input("Enter Second Operand :"))
        if ex == '+':
            print(f"Answer :{add(no1,no2)}")
        elif ex== '-':
            print(f"Answer :{dif(no1, no2)}")
        elif ex == '*':
            print(f"Answer :{mul(no1, no2)}")
        elif ex== '/':
            print(f"Answer :{div(no1, no2)}")
        else:
            print("Invalid Operation")
        op=input("Enter y fo Continue otherwise n :")
        if op == 'n':
            eop=False
        else:
            cal()
cal()