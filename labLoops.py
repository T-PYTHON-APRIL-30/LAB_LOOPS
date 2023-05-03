print("------- ( 1 ) -------")
print()
for i in range(45,211):
     if i == 100:
        continue
     if i == 206:
        break
     print(i, end=" ")

print()
print("------- ( 2 ) -------")
print()
userIns = int(input("What is the product of 7 * 24 ? "))

while userIns != 168 :
    print()
    print("Your Answer is wrong try again..")
    print()
    userIns = int(input("What is the product of 7 * 24 ? "))
else:
    print()
    print("You answered this Question correctly (;")

print()
print("------- ( Bonus ) -------")
print()

userInputs = int(input("Enter a positive integer: "))
sum = 0 
for num in range(0,userInputs,2) :
    num+=2
    sum += num
print(f"The sum of even numbers between 1 and {userInputs} is {sum}")