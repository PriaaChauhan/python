# # write a code of capitalizind each initials of the string- (dont use title())

# x  = "hello ladies and gentlemen"
# x2 = []
# y = x.split()
# print (y)
# for i in y:
#     print(i)
#     z = i.capitalize()
#     x2.append(z)
#print(" ".join(x2))
    
# # extract all letters before @  from email id 

sample = "pria@gmail.com"
sample2 = sample.find("@")
print(sample2)
print(sample[:sample2])

# # remove duplicate item from list 
list = [1,1,2,2,3,3,4,4]
list2 =[]
for i in list:
   if i not in list2:
       list2.append(i)
print(list2)       

