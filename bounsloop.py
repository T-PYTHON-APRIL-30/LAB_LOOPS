num= int(input("Please enter the positive number: "))
x= 0
for number in range (1 , num+1):
    if number%2==0:
        print(number)
        x += number
print("The sum of number = ", x)
