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


#continue statement


def demo1():
    for x in range(11,20):
        if(x%2 == 0):
            continue
        print(x)
demo1()

#enumerate function

def days():
    day = ['bappa','abir','shimul']
    for i,d in enumerate(day):
        print(i, d)
days()
