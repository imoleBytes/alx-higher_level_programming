

def check(**kwargs):
    print (kwargs)
    for i in kwargs.items():
        print(i)

    # print(args[1])


check(name="mike", age=18)
# print()