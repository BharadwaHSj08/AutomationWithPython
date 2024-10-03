def myfuntion():
    global x
    x="Awesome"

    print("Python is " +x)

myfuntion()

print("Python is " +x)

print("----------------------------------------------------")

#we can also change the Global Variable in this way

y="Poor"

def yourfunction():
    global y
    y="Good"

    print("Python is " +y)
yourfunction()

print("Python is " +y)

