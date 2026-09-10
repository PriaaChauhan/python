# # IMPORTANT RULES OF SETS YOU MUST KNOW 
    # 1. sets do not allow mutable data types
    # 2. sets itself a mutable data type
    # 3. sets do not allow duplicates
    # 4. sets have no idenxing and slicing no accessing no editing
    
# # CREATE A SET
# empty set 
S1 = {}
print(type(S1)) # its output will be dictionary , as this is  the deafult behaviour in pyhton , so we cant make an empty sets in this way

S2 = set()
print(type(S2))  #thats how we make an empty set using set( function)

# heterogenous set
S3 = {1,2,3,"hello"}

# homogeneous set
S4 = {"a","b","c","d"}

# # DELETE SETS
# del() - it will delet whole set
S5 = {1,2,3}
del(S5)
# print(S5)

# remove -  delete one item
S6 = {5,6,7,8}
S6.remove(5)
print(S6)

#pop() - remove last element of set 
S7 = {55,66,77,88}
S7.pop()
print(S7)

# # OPERATIONS
#  concatenation and multiplication dont work here, but looping and membership opertaor does
S8 = {34,24,56,43,21,12,14}
for i in S8:
    print (i)
    
print(56 in S8) #true

# # FUNCTIONS

S9 = {2,1,3,5,4,6}
S10 = { 222,333,444,555}

print(min(S9))
print(max(S9))
print(len(S10))
print(sorted(S9))
print(sum(S10))

# certain function that only sets can use
Set1 = {1,2,3,4,5}
Set2 = {4,5,6,7,8}

# union - mix and not repeat dupliactes
print( "union", Set1.union(Set2))

# intersection - print only repeat elements
print(  "intersecion",Set1.intersection(Set2))

# difference - elemnet jo set1 me hai but set 2 me nahi hai
print(Set1.difference(Set2))

# difference - elemnet jo set2 me hai but set 1 me nahi hai
print(Set2.difference(Set1))

# symmetric difference - remove same elements (jo dono me h)
print(Set1.symmetric_difference(Set2))

# disjoint -  checks if there is any same element in sets or not , if not - gives true, if yes - gives false
print(Set1.isdisjoint(Set2))

# issuperset
Set3 ={1,2,3,4}
Set4 = {1,2,3,4,5,6,7}
print(Set4.issuperset(Set3))
print(Set3.issuperset(Set4))

# issubeset
print(Set3.issubset(Set4))
print(Set4.issubset(Set3))
