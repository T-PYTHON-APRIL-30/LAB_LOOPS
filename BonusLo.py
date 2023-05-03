num = "enter a positive int"
numi = int(input(num))
evensum = 0
for number in range(1,numi+1):
    if number%2 == 0:
        evensum += number
 
print(evensum)
