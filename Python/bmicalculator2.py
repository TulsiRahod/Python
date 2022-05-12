weight=input("Enter Your Weight in KG :")
height=input("Enter Your height in Meter :")

bmi=int(weight)/float(height)**2
bmi_int=int(bmi)

print(bmi_int)

if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal Weight")
elif bmi<30:
    print("Overweight")
elif bmi<35:
    print("Obese")
else:
    print("Clinicly obese")