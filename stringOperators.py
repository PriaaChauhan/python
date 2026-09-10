# ------------------------1 Arithmetic Oprators-------------------------------
# (a)  +
# (b)  *

print("Hello" + " "+ "World")
print ("Hello" *3)



#  --------------------------2 Relational / Comparison Operators-------------------------------

# this is due  to lexiographical comparison of strings, where the first character of each string is compared based on their unicode values. Means alphabetical order is followed. jo letter pehle ata hai wo chhota hi hhoga humesha, for example =  a < b, b < c and most importantly , capital letters are smaller than small letters, so A < a, B < b, C < c and so on. 


a = "goa" > "kolkata"
print(a)

b = "kerala" > "Kolkata"
print(b)

c = "bihar" < "Bihar"
print(c)


#  ---------------------------3 Logical Operators-------------------------------
#  " " -  false,  "non-empty string" - True,  "0" - True,  "1" - True,  "None" - False,  "False" - True,  "True" - True

print("" and "ok")
print ("hello" and "world")
 
print("hello" or "world")
print("" or "world")

print(not "hello")
print(not "")


# ----------------------------4 Membership Operators-------------------------------

c = "call me pria ji"
for i in c[2:7:1]:
    print(i)
 
print("pri" in c) 
print("pria" not in c)