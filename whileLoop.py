# When do we actually use while?

# The important part is that you don't always know exactly how many times the loop needs to run.
# "keep repeating while condition become true"
  
#PROBLEM 1 - until and unless user enters correct password - repeat the question 
password = input("enter password : ")
while password != "123":
   password = input("enter pasaword again bro : ")

print("correct password")
 

# PROBLEM 2 -  read all elements of list to the last

list1 = [1, 2, 3, 4, "hey", "pria", "oho"]

i = 0

while i < len(list1):
    print(list1[i])
    i = i + 1

# Problem 3 — Print only even numbers
list2 = [1,2,3,4,5,6,7,8,9,10]
i = 0

while i < len(list2):
    if list2[i] % 2 == 0:
        print(list2[i])

    i = i + 1


# Problem 4 — Count items in a list

items = ["apple", "banana", "mango", "orange", "grapes"]

i = 0
count = 0

while i < len(items):
    print(items[i])
    print(count)

    i = i + 1
    count = count + 1

print("total items", count)