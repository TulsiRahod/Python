height=int(input("Enter Your height: "))
bill=0
if height>120:
    print("you can ride!")
    age = int(input("Enter your age :"))
    if age<12:
        bill=5
    elif age<18:
       bill=7
    elif age>=45 and age<=55:
        bill=0
        print("Enjoy free ride!!!!")
    else:
       bill=12

    photo = input("Enter 'Y' for Photo and 'N' for Not")
    if photo == 'y':
        bill = bill + 3

        print(f"Your Final Bill is {bill}$")
else:
    print("Sorry You can`t ride")


