'''
Sum of Even Numbers

Write a Python program that prompts the user for a positive integer n, and then calculates the sum of all even numbers between 1 and n, inclusive.

Your program should use a loop (either a for loop or a while loop) to iterate over the numbers between 1 and n, and only add the even numbers to the sum.

For example:

Enter a positive integer: 10
The sum of even numbers between 1 and 10 is 30.
In this example, the even numbers between 1 and 10 are 2, 4, 6, 8, and 10, and their sum is 30.

'''
print()
print("-"*60)
print()
n = int(input("Enter a positive integer: ")) 
adjust = n + 1
i = 0
number = 0
for i in range(adjust):
   if (i % 2 == 0):
    number += i
print(f"The sum of even numbers between 1 and {n} is {number}.")
print()
print("-"*60)
print()
