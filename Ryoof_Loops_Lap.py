# LAB_LOOPS



# 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the 
#sequence and print the elements. Skip the number 100 and break the loop at 205


for number in range(45, 210):
    if number == 100:
        continue

    elif number == 205:
        break
    print(number)

## 2) Using a while loop and input , do the following :
#- Ask the the user : "what is the product of 7 * 24 ?"
#- check if the answer is right then exit the loop and print "You answered this Question correctly"
#- if the answer is wrong, then print "Your Answer is wrong try again.." 
# and show the user the question again.

question: str ="what is the product of 7 * 24 ?"

while int(input(question)) != 7*24:
    print("Your Answer is wrong! try again..")
else:
    print("You answered this Question correctly")

#طريقة ثانية
while True:
    user_answer=input(question)
    if user_answer.isdigit() and int(user_answer)== 7*24:
        print("you answered this Question correctly")
        break
    else:
        print("Your Answer is wrong! try again..")