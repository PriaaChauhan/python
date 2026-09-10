# # Dictionary is very special data type which is havinf key-value pairs 
# # important rules about dictionary
    #1.  dictionary is mutable data type
    #2.  keys are always immutable but values can ne mutable
    #3.  indexing is not possible 
    #4. keys should be unique or should be immutable data type
    
# CREATE A DICTIONARY

#  Empty dictionary
D = {}

# simple dictionary
D1 = {"name": "Pria"}
4
# we cant use any mutable data type in key
# D3 = {[1,2]: "priya"}
# print(D3) # it will throw an error bcz list is mutable data type

D4={(1,2): "priyaasasa"}
print(D4)

# key shoud be unique
D5 = {"name":"pria", "name" : "priya"}
print(D5) # it will print priya only , as it updates name to priya 

#  acess value from dict (there is only one way)
D6 = {"name": "priya" , "gender":"female"}
print(D6["name"])

# editing dict
D7 ={"name": "neha"}
D7["name"] = "pria  ji"
print(D7)

# looping
D8 = {"name": "priya" , "gender":"female","age":26}
for i in D8:
    print (i) # it will print keys only , therec is anotehr way toh write value
    print(i,D8[i]) # this is how you print values
print(D8.keys()) # this function eill give list of keys
print(D8.values()) # this function eill give list of values