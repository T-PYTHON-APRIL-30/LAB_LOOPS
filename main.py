#Q1:
for num in range(45, 210):
    if num == 100:
        continue
    elif num == 205:
        break
    print(num)

print("_"*10)

#Q2:
q = ("what is the product of 7 * 24 ?")

while int(input(q)) != 168:
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")