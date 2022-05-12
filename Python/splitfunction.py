import random
name=input("Enter Names :")
names=name.split(",")
#
# print(names)
#
# x=len(names)
# y=random.randint(0,x-1)
#
# print(names[y])
person=random.choice(names)
print(person)

