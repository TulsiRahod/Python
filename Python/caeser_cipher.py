letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



def encrypt(message,key):
    cypher=""
    for letter in message:
        position=letters.index(letter)
        new_position=position+key
        new_letter=letters[new_position]
        cypher+=new_letter
    print(f"Encoded Message Is {cypher}")

def decrypt(message,key):
    plain=""
    for letter in message:
        position=letters.index(letter)
        new_position=position-key
        new_letter=letters[new_position]
        plain+=new_letter
    print(f"Decoded Message Is {plain}")

def caeser(message,key,direction):
    cypher = ""
    for letter in message:
        if letter in letters:
            position = letters.index(letter)
            if direction == "encode":
                new_position = position + key
            elif direction == "decode":
                new_position = position - key
            new_letter = letters[new_position]
            cypher += new_letter
        else:
            cypher+=letter
    print(f"Encoded Message Is {cypher}")
x='yes'
while(x=='yes'):
    direction = input("Type 'encode ro Encrypt and 'decode' to Decrypt :")
    text = input("Enter Your Message :").lower()
    shift = int(input("Enter Key :"))
    shift = shift % 26
    caeser(message=text, key=shift, direction=direction)
    x=input("You Want to continue type 'Yes' else 'No' :")

# if direction=="encode":
#     encrypt(message=text, key=shift)
# elif direction=="decode":
#     decrypt(message=text, key=shift)

