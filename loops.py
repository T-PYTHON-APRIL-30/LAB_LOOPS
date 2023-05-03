#Using range()
print("Range:")

numbers_range = range(45, 210)

for number in numbers_range:
    if number == 100:
        continue

    if number == 206:
        break
    print(number, end=" ")


#Using a while loop and input



Qustion1 = "what is the product of 7 * 24 ?? "


while input(Qustion1) != "168":
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")

