def main():
    x, y = 1000, 100
    if(x < y):
        st = "x is less than y"
    elif(x == y):
        st = "x and y are same"
    else:
        st = "x is greater than y"
    print(st)

main()

def main1():
    x, y = 20, 100
    st = "x is less than y" if (x<y) else "x is greater or equal to y"
    print(st)
main1()