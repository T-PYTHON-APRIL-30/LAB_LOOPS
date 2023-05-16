## Sum of Even Numbers


# Write a Python program that prompts the user for a positive integer `n`,
#and then calculates the sum of all even numbers between 1 and `n`, inclusive.

number = int(input("Enter a positive integer: "))
while number % 2 == 0:
    print("number {0} is an even number".format(number))
    break
else:
    print("number {0} is an odd number".format(number))

sum_num=0
for number in range(number):
    if number % 2 == 0 :
        sum_num = sum_num + number
print(f"The sum of even numbers between 1 and {number} is:{round(sum_num)}")



