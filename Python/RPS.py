import random

rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice=[rock,paper,scissors]
user=int(input("0 For Rock ,1 For Paper ,2 For Scissors :"))
com=random.randint(0,2)
print(f"Your Choice\n{choice[user]}")
print(f"Computer Choice\n{choice[com]}")

if user==com:
    print("Match Is Draw!!")
elif user==0 and com==1:
    print("You Lose!!!")
elif user==1 and com==2:
    print("You Lose!!!")
elif user==2 and com==0:
    print("You Lose!!!")
else:
    print("You Win!!!")
