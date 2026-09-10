# 1. default arguments
# 2. positional arguments
# 3. keyword arguments
# 4. arbitrary arguments

# major difference between agruments and parameter are  - Arguments are the actual values, parameters are the placeholders that take arguments as their value.


#if we do not provide value to parameter , or not give arguments , code will crash, for this we use -  

# DEFAULT ARGUMENTS - by using them , even if we does not pass anything to function (power()) , it will not crash the code, it will go with the default values. 

def power(a =1, b = 2):  # these are default arguments 
    return a*b  # 1*2 =2
print(power())

def power_(g=3, h= 3):
    return g*h  # 6*3 =  18
print(power_(6)) # it will print 18 , as by default usne  g ko 6 liya & h ko 3 le liya without crashing code




#  POSITIONAL ARGUMENTS -  Positional arguments mean values are passed in the same order as parameters are defined in the function.
# The first value goes to the first parameter, second to the second and so on.



# KEYWORD ARGUMENTS - Keyword arguments mean you pass values by parameter names while calling the function.
# The order does not matter as long as the names are correct.
# Defaults are used if some arguments are not provided.
# This makes the code more readable and less error-prone.

def nameAge(name, age):
   return("Hi, I am", name , "My age is ", age)
print(nameAge(age=20, name="Prince")) # it will override the positional arguments as we call them explicitely



# ARBITRARY ARGUMENTS - arbitrary arguments allow a functi   on to accept an indefinite number of inputs, which is highly useful when you do not know in advance how many values a user will pass.
#  Python provides two ways to handle these variable-length inputs: *args for positional arguments and **kwargs for keyword arguments

def arb(*num):
    result = 1
    for i in num:
        result *= i
    print(result)
    return result

print(arb(19, 3 , 2))