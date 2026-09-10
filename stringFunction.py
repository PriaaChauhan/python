# common functions 
# 1. len -  give length of string
# 2. min -  give minimum character in string based on ASCII value
# 3.  max -  give maximum character in string based on ASCII value
# 4.  sorted -  return a new sorted list of characters in string based on ASCII value and return a list

c = "hyderabad"
print(len(c))
print(min(c))
print(max(c))
print(sorted(c))
print(sorted(c,reverse=True))

# THESE FUNCTION CAN ONLY BE APPLIED ON STRINGS

print(c.capitalize())
print(c.title())
print(c.upper())
print(c.swapcase())

a = "it is raining outside"
print(a.count("i"))
print(a.count("ra"))
print(a.count("h")) 


# # diff btw find and index is , if value is not present in string , find returns -1 and index throws an error

b = "today is a good day"
print(b.find("ts"))
print(b.find("day"))

print (b.index("day"))
print(b.index("ts")) 


# # stratswith & endswith
  
d = "hello world hey"
print(d.startswith("hello"))
print(d.startswith("hey"))

print (d.endswith("hey"))
print(d.endswith("hello"))

# #FORMAT() - many ways to use this

e = "hello my name is {} and age is {}"
print(e.format("pria", 24))

f = "hello my name is {1} and age is {0}"
print(f.format("pria", 24 ))

g = "hello my name is {name} and age is {age}"
print(g.format(name ="pria", age = 24 ))

# # split and join -  split converts string into lists , and join converts lists into string

h = " company name is orinet"
print(h.split())
print(h.split("is"))
print(h.split("a"))

i = ["my", "fav", "color", "is", "black"]
print(" ".join(i))

# # replace()

j = "my brother is really funny"
print(j.replace("brother", "father"))
print(j.replace("i", "w"))

# # strip  
k = "                hello                 "
print(k.strip())