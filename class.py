class sample():
    def demo1(self):
        print("This a base method")
    def demo2(self,string):
        print("This is extended method "+string)

def main():
    bappa = sample()
    bappa.demo1()
    bappa.demo2("This is bappa")

main()