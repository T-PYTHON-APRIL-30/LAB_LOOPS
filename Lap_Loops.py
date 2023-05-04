#Using for Loop
for numbers in range(45,210):

    if numbers == 100:
        continue

    if numbers == 205:
        break

    print (int(numbers))

print("__"*15), print()

#Using while loop 

while int(input("what is the product of 7 * 24? ")) != 168:

    print("Your answer is wrong try again!")

else:
    print("You answered this question corrctly")