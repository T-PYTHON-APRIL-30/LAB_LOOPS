number = ("Enter a positive integer: ")
userNumber = int (input(number))
Total = 0
for i in range(1,userNumber+1) :
    if (i%2 == 0):
        Total = Total + i
        
print (f"The sum of even numbers between 1 and {userNumber} is {Total}")    
    
      