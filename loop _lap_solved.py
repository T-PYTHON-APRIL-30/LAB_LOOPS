#1)Using range(), make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205
2#) Using a while loop and input , do the following :

#Ask the the user : "what is the product of 7 * 24 ?"
#check if the answer is right then exit the loop and print "You answered this Question correctly"
#if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.



#task1 
for number in range (45 , 210):
    print (count)
    if  number == 100:
        continue
    if number == 205:
        break
    print (number)

#task2
question : str = "what is the product of  7 * 24 "

while int (input(question)) != "168":
    print ("tour answer is wrong ! try again")
else:
    print ("You answered this question correctly! *_*")


#bounce:
user_number =int(input("please provied number"))

total_sum = 0
for number in range(1,user_number+1):
    if number%2 ==0:
        total_sum +=number
print("total sum of  even numbers betwen 1 and (user_number) is (total_sum)")


