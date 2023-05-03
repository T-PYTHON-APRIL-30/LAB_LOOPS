nump_range = range(45,210) 
for numpers in nump_range: 
    if numpers == 100:
        continue
    if numpers == 205:
        break    
    print (numpers, end = " | ")
print ("")    

Question  = "what is the product of 7 * 24 ? "

while   int (input (Question)) != 168 :
    print ("Your Answer is wrong try again..")
else :
    print ("You answered this Question correctly")
