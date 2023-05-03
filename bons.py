'''
Sum of Even Numbers
Write a Python program that prompts the user for a positive integer n, and then calculates the sum of all even numbers between 1 and n, inclusive.

Your program should use a loop (either a for loop or a while loop) to iterate over the numbers between 1 and n, and only add the even numbers to the sum.

'''


Inputs = int(input("Enter a positive integer: "))

sum_number = 0 

for num in range(0,Inputs,2) :
    num+=2
    sum += num

print(f"The sum of even numbers between 1 and {Inputs} is {sum}")