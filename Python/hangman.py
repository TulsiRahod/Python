import random
from hangman_art import logo,stages
print(logo)
from hangman_word import word_list
choose=random.choice(word_list)


raw=[]
for _ in choose:
    raw+="_"
eog=False
lives=6

while not eog:
    guess=input("Guess a letter :").lower()
    for position in range(len(choose)):
        letter =choose[position]
        if letter == guess:
            raw[position]=letter

    if guess not in choose:
        lives-=1
        print(stages[lives])
        if lives==0:
            print("You Lose!!")
            print(choose)
            eog=True

    if guess not in choose:
        print("You Choose Wrong!!")
    else:
        print("You Choose Right!!")
        print(f"{' '.join(raw)}")

    if "_" not in raw:
        eog=True
        print("You Win!!")





