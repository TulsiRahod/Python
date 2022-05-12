print("Welcome To Tip Calculator")
bill=float(input("What was the total bill :"))
tip=int(input("What percentage tip would you like to give :"))
people=int(input("How many people should pay :"))

ptip=tip/100
totaltip=bill*ptip
totalbill=bill+totaltip

per_person=totalbill/people

print(f"Each person Shiuld Pay :{per_person}")