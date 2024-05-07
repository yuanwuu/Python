# recursive function: fn that call itself

def add_one(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)  # it calls itself until the total = 9
    # add_one(total)  # w/o the return keyword, output will be None


mynewtotal = add_one(0)
print(mynewtotal)  # this return 10

print('\n' + 'for...in loop')
for x in range(1, 11):
    if (x >= 11):
        x + 1
    print(x)
