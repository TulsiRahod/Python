height=int(input("Enter Your height: "))

if height>120:
    print("you can ride!")
    age = int(input("Enter your age :"))
    if age<12:
        print("You have to pay 5$")
    elif age<18:
        print("You have to pay 7$")
    else:
        print("You have to pay 12$")

else:
    print("Sorry You can`t ride")