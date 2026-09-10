# A local variable is created inside a function and is normally available only within that function. A global variable is created outside functions and can be accessed throughout the program. The global keyword can be used when a function needs to modify a global variable.

LOCAL VARIABLE
───────────────
Created inside a function

def test():
    x = 10

x is LOCAL


GLOBAL VARIABLE
───────────────
Created outside a function

x = 10

def test():
    print(x)

x is GLOBAL


READ GLOBAL
───────────
x = 10

def test():
    print(x)


MODIFY GLOBAL
─────────────
x = 10

def test():
    global x
    x = 20