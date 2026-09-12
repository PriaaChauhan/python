# Think of it like:

# TRY: "Run this code."
# EXCEPT: "If something goes wrong, don't crash—do this instead."

#  suppose - if user write " hello" in input , it will throw error and code will crash - 

age = int (input("enter you age")) 

# but we call handle this try and except like 
try:
    age = int(input("Enter your age: "))
except:
    print("Please enter a number")

