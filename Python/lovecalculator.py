print("Welcome To Love Calculator")
name1=input("Enter Your name :")
name2=input("Enter Your partner`s name :")
both=(name1+name2).lower()

t=both.count("t")
r=both.count("r")
u=both.count("u")
e=both.count("e")

l=both.count("l")
o=both.count("o")
v=both.count("v")

true=t+r+u+e
love=l+o+v+e

truelove=str(true)+str(love)
trueloveint=int(truelove)

if trueloveint<10 or trueloveint>90:
    print("You are both Like Mentos And Coke")
elif trueloveint>=40 and trueloveint<=50:
    print("Both of you look Pretty together")
else:
    print("You are Normal Couple")