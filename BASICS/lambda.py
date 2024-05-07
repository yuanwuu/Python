# LAMBDA format: lambda + param(s) : operation

from functools import reduce


def multiple(a): return a*2
# lambda a : a*2


# lambda a,b : a*b
def dual_params(a, b): return a*b


print(multiple(10))  # 10
print(dual_params(2, 4))  # 8


def funcBuilder(x):
    return lambda num: num + x


add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))  # 17
print(add_twenty(7))  # 27

########################


numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

###############################

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

#############################


numbers = [1, 2, 3, 4, 5, 1]
# lambda acc, curr: acc(sub-total) + curr(current val)
total = reduce(lambda acc, curr: acc + curr,
               numbers, 10)  # 10 is a starting value

print(total)

print(sum(numbers, 10))


names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
