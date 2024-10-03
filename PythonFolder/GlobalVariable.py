#Defined outside a function
x="awesome"

def myfunc():
    #defined inside a function and it is a local keyword
    x="Good"
    print("Python is " +x)

myfunc()

print("Python is " +x)
