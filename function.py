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

def power(num,x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(3))
print(power(3,4))
print(power(x=4,num=3))

def mult_add(*args):
    result = 0
    for i in args:
        result += i
    return result
print(mult_add(10,20,40))
print(mult_add(100,200))