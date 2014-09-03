#define a function by def keyword
#each statement indented by 2 space corresponding
# that function and also a column after the parenthesis

def bappa():
    print("This is python function")
#bappa()

print(bappa())  # print statement and return the value -> none

print(bappa)  # print as an object

def bappa(arg1,arg2):
    print(arg1," ",arg2)

bappa(20,30)
print(bappa(20,30))

def cube(x):
    return x*x*x
print(cube(20))