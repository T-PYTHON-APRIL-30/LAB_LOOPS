number:int =input("Enter a positive integer: ")
if int(number) <=0:
    print("only for positive number ")
sum=0
for num in range(1,int(number)+1):
    if num % 2 ==0:
        print(num,end=" ")
        sum =sum+num

print(f"the sum is : {sum}")