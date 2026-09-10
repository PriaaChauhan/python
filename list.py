  # DIFF BTW ARRAYS AND LISTS

  # 1. array is homogeneous, meaning it can only contain elements of the same data type, while a list is heterogeneous and can contain elements of different data types.
  
  # 2. array is more memory efficient than a list, as it uses less memory to store the same number of elements.
  
  # 3.arrays are much faster than lists for numerical operations, as they are optimized for such operations.
  
  # 4. Lists are more programmer friendly
  
  
# HOW TO CREATE A LIST

#1. empty list 
L = []

# 2. heterogeneous list (which contains different data types)
L1 = [1, 2.5, "hello", True]
    
#  3.  homogeneous list (which contains same data types)
L2 = [1, 2, 3, 4, 5]

# 4. 2D list (which contains lists as elements)
L3 = [[1, 2, 3], [4, 5, 6], [7, 9]]

# 5 . 3D list (which contains lists as elements)
L4 = [[[1, 2], [3, 4]], [[5,6]]]

# 6 . can also create list with type conversion function list()
L5 = list("hello") # output will be  ['h', 'e', 'l', 'l', 'o']

# HOW TO ACCESS ELEMENTS OF A LIST
print(L2[::-1])
print(L2[0]) 
print(L2[1:4])
print(L3[1][2])

# HOW TO MODIFY ELEMENTS OF A LIST
# --- lists are mutable, meaning we can change their elements after they are created.
L2[0] = 10
print(L2)
L4[0][1][1] = 88
print(L4)
L2[0:3]= [100, 200, 300]
print(L2)
L2.append(201) # add one element to the last 
print(L2)
L2.extend([202, 203]) # add multiple elements to the last
print(L2)
L2.extend("hello") # add multiple elements to the last, but each character of the string will be added as a separate element
print(L2)
L2.insert(3, 99) # add element to the desired  position
print(L2)

# HOW TO DELETE ELEMENTS FROM LIST - 5 ways
# 1. delete


# 2. remove - use when you dont know the the element index
L10 = [1,2,3,4,"hello", "world"]
L10.remove("hello")
print(L10)

# 3. pop -  delete last element of the list
print(L10.pop())
print(L10)


# 4. clear  - make list elmpty
L10.clear()
print( "empty list", L10)


# 5. del
del L2[3]
print(L2)

# OPERATIONS IN LIST
list_1 = [2,5,6,1,4,3,8,0,56]
list_2 = [1,2,3,[6,7],[34,1]]

print(list_1+list_2)
print(list_1*2)
for i in list_2:
    print(i)
    

# # FUNCTIONS IN LISTS - len,min,max etc

list_3 = [100,200,300,400, 4, 500,600]
print(min(list_3))
print(max(list_3))
print(len(list_3))
print(sorted(list_3))
print(sorted(list_3, reverse = True))
list_3.sort()
print(list_3) # diff btw sorted and sort is - sorted gives new listand sort make changes in original list




