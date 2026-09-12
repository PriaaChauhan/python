# 📖 Reading files → File Input
# ✍️ Writing files → File Output
# 📖✍️ Reading + Writing → File Handling / File I/O


# "w" → write/replace
# "a" → append/add to existing content
# "r" → read

# READING - it will read the data from "data.txt" file
with open("data.txt", "r") as file:
    content = file.read()

print(content)

# WRITING -  it will make one file name "data2.txt" and write data here  but if data2.txt exist already , it overrides that file and replace new content
with open ("data2.txt", "w") as file:
    file.write("helllloooo hihi huhu hohoho")
 

#APPEND -  it will add content to the file  , it says -"give me this file and add new stuff at the end."
with open ("data2.txt", "a") as file:
    file.write("okay")

# .append() is not any function in file , thats why we use file. write() bus use "a" instead of "w " 

# JSON READ AND WRITE 
# but what if we red and write data in JSON file ? 


import json

data = {
    "name" : "Priya Chauhan",
    "age" : 24
}

with open ( "data.json", "w") as file: #If data.json doesn't exist → Python creates it.
    json.dump(data, file) # it means "Take data and put it inside file as JSON."


#json.load()
# 1. "r" → open the file for reading
# 2. json.load(file) → take the JSON from the file and convert it into a Python dictionary

with open("data.json", "r") as file:
    data = json.load(file)

print(data)



# MAIN POINTS
# JSON file → Python
# json.load()

# Python → JSON file
# json.dump()