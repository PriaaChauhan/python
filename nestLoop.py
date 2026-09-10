for i in range (1,6):
    pass
    print (i)
    
print("--------------------------")
    
for i in range (1,15):
    if i == 8 : 
     break
    print (i)
        
print("--------------------------")

for i in range (1,15):
    if i == 8 : 
     continue
    print (i)
    
print("--------------------------")    

rows = int (input("enter the num of rows"))

for i in range (1, rows+1):
    for j in range(1 , i+1):
        print("*", end=" ")
    print()