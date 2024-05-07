users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Elsa')
# print(users)

users += ['Jason']
# users += 'Jason' #output: 'J','a','s','o','n'

print(users)

users.extend(['Robert', 'Jimmy'])
# print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')  # at 0 index, add str 'Bob'
# print(users)

# starting at index 2 and ends at 2, add the list of strs
users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
# print(users)

users.remove('Bob')  # 'Bob' at index 0 will be removed
# print(users)

print(users.pop())  # last str will be pop off
# print(users)

del users[0]  # del. the str in idx 0 from the users list
# print(users)

# del data
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
# print(users)

users.sort(key=str.lower)
# print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()  # [5, 1, 78, 42, 4]
# print(nums)

# nums.sort(reverse=True) # [78, 42, 5, 4,1] order decending, og. list modified
# print(nums)


print(sorted(nums, reverse=True))  # [78, 42, 5, 4,1] no change in og. list
# print(nums)

numscopy = nums.copy()  # make a copy of the numg
mynums = list(nums)  # 'list' is the constructor and nums will be a in a list
mycopy = nums[:]  # a copy of the og. list

# print(numscopy)  # make copy method 1
# print(mynums)  # make copy method 2
# mycopy.sort()  # sort the list before the copying
# print(mycopy)  # make copy method 3
# print(nums)

print(type(nums))

mylist = list([1, "Neil", True])  # create a list w mix data types
print(mylist)

# Tuples

mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

# print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)  # 1
print(two)  # [4,2]: *print the rest list
print(hey)  # 8

print(anothertuple.count(2))  # 3, count the occurence of 2
