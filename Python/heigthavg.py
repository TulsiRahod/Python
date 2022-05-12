students_heigth=input("Enter Students Heights :").split()

# for x in range(0,len(students_heigth)):
#     students_heigth[x]=int(students_heigth[x])
#
# print(students_heigth)
#
# print(len(students_heigth))

count=0
sum=0

for y in students_heigth:
    sum+=int(y)
    count+=1

print(sum)
print(count)
average=sum/count
print(f"Average Of Students Height is {average}" )