for number in range(45,210):
    if number==100:
        continue
    print(number,end=" ")
    if number==205:
        break
print()
print("---"*15)
while int(input("what is the product of 7 * 24 ?"))!=168:
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")