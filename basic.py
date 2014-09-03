#variable
a = 20
print(a)

#string
a = "home"
print(a)

# a comment by # sign

#function define

def demo():
    b = 20
    print(b)

demo()

#local variable

def apple():
    a = 30;
    print(a)
apple()
#give 30 as output
print(a)
#give home as output

#global variable

def mango():
    global a
    a = 50
    print(a)
mango()
print(a)

#delete definition by del keyword

del a
print(a) #cause error because a is now unknown