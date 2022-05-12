def format_name(first,last):
    f=first.title()
    l=last.title()
    return f+" "+l

fname=input("Enter First Name :")
lname=input("Enter Last Name :")
fullname = format_name(fname,lname)
print(fullname)