'''
# LAB_LOOPS

## 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205

## 2) Using a while loop and input , do the following :
- Ask the the user : "what is the product of 7 * 24 ?"
- check if the answer is right then exit the loop and print "You answered this Question correctly"
- if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.
'''
for item in range(45, 210):
    if item == 100:
        continue
    if item == 205 :
        break
    print(item)

Sol : str =""


while True:
    Sol = input("what is the product of 7 * 24 ? (please enter integer number)")
    if not Sol.isdigit() :
        continue
    if int(Sol) == 168 :
        print("You answered this Question correctly")
        break
    print("Your Answer is wrong try again..")
    


'''
## Bonus

### Sum of Even Numbers

Write a Python program that prompts the user for a positive integer `n`, and then calculates the sum of all even numbers between 1 and `n`, inclusive.

Your program should use a loop (either a `for` loop or a `while` loop) to iterate over the numbers between 1 and `n`, and only add the even numbers to the sum.

For example:

```
Enter a positive integer: 10
The sum of even numbers between 1 and 10 is 30.
```

In this example, the even numbers between 1 and 10 are 2, 4, 6, 8, and 10, and their sum is 30.

'''

n : str = input("Enter a positive integer: ")
while not Sol.isdigit() :
    n = input("Enter a positive integer: ")
sum : int = 0
for n in range(0, int(n)+1, 2):
    sum += n

print(f"The sum of even numbers between 1 and 10 is {sum}")
