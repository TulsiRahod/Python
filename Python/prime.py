number=int(input("Enter Number :"))
def prime_check(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1

    if flag==0:
        print(f"{n} is Prime Number")
    else:
        print(f"{n} is not Prime Number")

prime_check(number)