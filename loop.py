#for loop
def apple():

    y = 1
    for y in range(5,10):
        print(y)
apple()

#for loop for collection
def simple():
    names = ["bappa","abir","sumon"]
    for n in names:
        print(n)
simple()

#break statement
def demo():
    for x in range(10,20):
        if(x==15):
             break
        print(x)
demo()
