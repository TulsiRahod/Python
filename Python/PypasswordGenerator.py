import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@','#','$','%','&','*','-','+','(',')']

print("Welcome TO PassWord Generator !!\n")
let=int(input("Enter How many Letters You want\n"))
num=int(input("Enter How many Numbers You want\n"))
sym=int(input("Enter How many Symbol You want\n"))

#easy
easypass=""
# for x in range(0,let):
#     easypass+=random.choice(letters)
#
# for x in range(0,num):
#     easypass+=random.choice(number)
#
# for x in range(0,let):
#     easypass+=random.choice(symbol)

# print(easypass)

#hard
hardpass=[]
for x in range(0,let):
    hardpass.append(random.choice(letters))

for x in range(0,num):
    hardpass.append(random.choice(number))

for x in range(0,let):
    hardpass.append(random.choice(symbol))
random.shuffle(hardpass)
# print(hardpass)

password=""
for x in hardpass:
    password+=x
print(f"Your Password is {password}")
