num = int(input("Enter a positive integer: "))
i = 0
sum = 0

while i < num:
    i += 2
    sum += i
else:
    print(f"The sum of even numbers between 1 and {num} is {sum}")