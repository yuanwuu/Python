# function format: def + fn name(lowercase / with _ ) + ():
def hello():
    print("Hello World!")

# hello()


def sum(num1=0, num2=0):  # num1=0,num1 has a defaule val of 0
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = sum(7, 2)
print(total)


def multiple_items(*args):  # *args = "*" a range/some/few/unknown amt. args
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")


def mult_named_items(**kwargs):  # unknown # or keyword args
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="Gray")
