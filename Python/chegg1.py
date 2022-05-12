def encrypt(str):
    ans = ""
    for i in range(0, length):
        if str[i] == 'a':
            ans += '?'
        elif str[i] == 'e':
            ans += '!'
        elif str[i] == 'o':
            ans += '+'
        elif str[i] == 'u':
            ans += '-'
        elif str[i] == 'i':
            ans += '*'
        else:
            ans += str[i]
    print(ans)
def decrypt(str):
    ans = ""
    for i in range(0, length):
        if str[i] == '?':
            ans += 'a'
        elif str[i] == '!':
            ans += 'e'
        elif str[i] == '+':
            ans += 'o'
        elif str[i] == '-':
            ans += 'u'
        elif str[i] == '*':
            ans += 'i'
        else:
            ans += str[i]
    print(ans)
while(True):
    x = input("For Encrypt Enter 1 else 2:")
    str = input("Enter Message :").lower()
    length = len(str)
    if x == "1":
        encrypt(str)
    else:
        decrypt(str)