name = "Dave"
count = 1


def another():
    color = "blue"
    global count  # accessing the global count(line 2) before you can use it
    count += 1
    print(count)

    def greeting(name):
        nonlocal color  # use color in parent variable
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()
