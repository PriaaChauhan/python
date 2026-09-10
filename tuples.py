# # HOW TO CREATE AN EMPTY TUPLES - it is just same as list but with open brackets () , and little different

# TUPLES ARE READ ONLY DATA TYPE (IMMUTABLE)

## empty tuple 
T = ()

## heterogeneors tuple 
T2 = ("hello", 1,2,3.5)

## homogeneous tuple
T3 = (1,2,3,4,5,6)
  
## 2d tuple
T4 = (1,2, (3,4))

## 3d tuple
T5 = (1,2, (3,4,(5,6)))

## we cant form a single lement tuple without using comma
T6 = ("hello") # this data type will be str not tuple
print(type(T6))

TT = (1) # this data type will be int not tuple
print(type(TT))

T7 = ("hello", ) # this will be tuple datatype
print(type(T7))

## another way of creating tuple is by using tuple() function

T8 = tuple("PATNA")
print(T8)


## HOW TO ACCESS TUPLES - it is exactly same as lists - whi same slicing and all
T9 = (1,2,3,(6,7,(8,9)), "hello")
print(T9[2]) 
print(T9[::-1])
print(T9[-1:])
print(T9[:-1])   
print(T9[3][2][0])


## HOW TO EDIT TUPLES
 # - we cant edit tuples directly just like lists as they are IMMUTABLE (like strings) - this is the major DIFF BTW TUPLES AND LIST
  # we can only delete the whole tuple by del()  function only
  
T10 = (4,5,6)
del(T10)
# print(T10) 


# # OPERATION WE CAN PERFORM ON TUPLES - same as lists
T11 = (6,5,4,3)
T12 = (10,9,8,7)
print(T11 +T12)
print(T11 * 2)
for i in T11:
    print(i)
    
# # FUNCTION WE CAN PERFORM ON TUPLES - same as lists
print(max(T11))
print(min(T11))
print(sum(T11))
print(len(T11))