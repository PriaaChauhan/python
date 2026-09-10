import sys
#   value of a in present is ROM , but if code runs it will come in ram ,  and it has its unique address ,  and "a" is poinitng towads it
#  id of a,b,c will be same , as they are poinitng to the same value
#  but if we chnage the value of a - its id will be chnage , but b and c is atill poinitng to the same value (45) so it still has same value

a = 45
b = a # this is called aliasing
a =  6 # id will change
c = b

print(id(a))
print(id(b))
print(id(c))
print(sys.getrefcount(a)) # this function gives you all the variable count which is poinintg to the value

#  BUT WHAT HAPPEN IF THERE IS  something stored in memory but usse koi bhi variable linked nahi hai , like what if we delete a,b,c all ???? then the value present in memory (without any reference)  is called garbage value,  here comes  GARBAGE COLLECTION, -  it is the process of cleaning this garbage from memory


# WEIRD BEHAVIOUR OF PYTHON -  from -5 to 256 , id will be same of all the variable if they are refferes to same value , but other than  -5 to 256 , id will chnage , for exaample

a = 2
b = 2
print(id(a))
print(id(b))


n = 2664
m = 2664

print(id(n))
print(id(m))


# if it is purely identifier than id will be same , if its not - id will be different

s = "hello_"
f = "hello_"
print(id(s))
print(id(f))

l = "hello ji n"
p = "hello ji n"
print(id(l))
print(id(p))

# CLONING IN LIST
# -  This method creates a new list by slicing all elements from the original. It’s concise and performs well.The [:] operator selects all elements and creates a new list, independent of the original.(kyuki cloning krne ke baad dono ka memory address different ho jata hai) - means a ka clone b krenge , or b change krenge toh a mein kuch change nahi hoga, kyuki memory address different h dono ka chahe mutable hai tab bhi

L = [1,2,3]
L2 = L[:] # ye krne se dono alag alag memory pe allocate ho jaynge, ek ke chnages doosre ko affect nahi karenge  
print(id(L))
print(id(L2))
 
L2.append(55)
print(L)
print(L2)

# NOTE:
# if we append in list, memory address will not change , but if we do concatenation -  address will definitely chnage , FOR EX.

list1 = [1,2,3]
print("id of list1  before append" , id(list1))
list1.append(34)
print(list1)
print("id of list1  after append" , id(list1)) # it will be same as before
 
#  in concatenation
list3 = [12,13,14]
print("id of list3  before concatenation" , id(list3))
list3 = list3 + [15,16]
print("id of list3 after concatenation" , id(list3)) # it will be different