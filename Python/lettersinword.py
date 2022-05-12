country=["india","iran","Africa","Japan"]

import random
choosen=random.choice(country)

guess=input("Guess A letter :").lower()

raw=[]
for _ in range(len(choosen)):
    raw+='_'
print(raw)

