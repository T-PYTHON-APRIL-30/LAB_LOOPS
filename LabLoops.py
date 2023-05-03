'''
1) Using range(), make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205
'''

number_range=range(45,210)

for number in number_range:
    if number == 100:
        continue
    if number == 205:
        break
    print(number, end=", ")


