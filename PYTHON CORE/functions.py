# function are nothing but a block of code having some purpose :
#  function me mainly do cheez important hai -  ABRSTRACTION & DECOMPOSITION

# ABSTRACTION -  Abstraction is the process of hiding implementation details and exposing only the essential functionality to the user.
# Tl;DR -   bas code run hona chahiye no matter uske ander sb kaise kaam kr rha hai , internal detais like print() function , we dont even know iska code kya hai , we just use this to print data whatever we want

# DECOMPOSITION - decomposition is the process of breaking one massive, hard-to-read function into multiple small, self-contained sub-functions. This increases readability, makes debugging easier, and promotes code reusability

 # example of finding odd and even numeber 
 # here def = keyword ,  is_even =  name of a function , num =  parameter/arguments and we can also add doocs in python function in three inverted commas , if someone wanna see what this function do , he or she will run  functionName.__ doc__
 
# if function is not returining anything, then by default it will be none, means it returns none

def is_even(num) :
  """ this function tells if a given number is even or odd """
  if type(num) == int :
    if num % 2 == 0: 
          return "Even"
    else :
        return "ODD"
  for i in range (1,20):
      print(is_even(i))
  else:
    return " not allowed"
    
print(is_even.__doc__)
print(type.__doc__)
print(list.__doc__) # it will give doc of list and type