fruits = ["apple","banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

q = 5
w = "John"
print(q,w)

#Global var

a = "awesome"

def myfunc():
    print("Python is " + a)

myfunc()

def myfunc2():
    a = "fantastic"
    print("Python is " + a)
myfunc2()

def myfunc3():
    global p 
    p = "fantastic"
myfunc3()

print("Python is " + p)