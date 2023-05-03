'''
Bonus
Sum of Even Numbers
Write a Python program that prompts the user for a positive integer n, and then calculates the sum of all even numbers between 1 and n,
 inclusive.

Your program should use a loop (either a for loop or a while loop) to iterate over the numbers between 1 and n,
 and only add the even numbers to the sum.

For example:

Enter a positive integer: 10
The sum of even numbers between 1 and 10 is 30.
In this example, the even numbers between 1 and 10 are 2, 4, 6, 8, and 10, and their sum is 30'''


num = int(input('Enter a positive integer: '))
sum = 0
for n in range (1,num+1):
    if n % 2 == 0:
        print(n)
        sum = sum + n

print(f'The sum of even numbers between 1 and {num} = {sum} ')
    #print(f'In this example, the even numbers between 1 and {num} are 2, 4, 6, 8, and 10, and their sum is 30')