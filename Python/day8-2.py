import math
h=int(input("Enter Height :"))
w=int(input("Enter Width :"))
coverage=5

def paint_calc(height,width,cover):
    paint=math.ceil(height*width/cover)
    print(f"You Need {paint} cans")

paint_calc(height=h,width=w,cover=coverage)