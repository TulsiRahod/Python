phone={"Iphone":"apple","Mi":"Poco","oppo":"OnePlus"}
print(phone)

phone["Vivo"]="Realme"
print(phone)

empty={}
# phone={}
# print(phone)

phone["Iphone"]="IOS"
print(phone)

for x in phone:
    print(x)
    print(phone[x])
    print()