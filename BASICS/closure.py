def parent_function(person, coins):
    # 'parent_function' is like a cookie cutter, defining the shape and ingredients.

    def play_game():
        # 'play_game' is like the cookie, made by the cutter, with its own unique details.
        # This allows the cookie (closure) to change its ingredients (variables).
        nonlocal coins
        # Change the number of coins (an ingredient) for this specific cookie.
        coins -= 1

        # The rest of the function prints out the state of the cookie's ingredients.
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game  # The cookie cutter returns a cookie.


# Creating cookies with different details (closures with different scopes).
tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

# Each cookie can be 'eaten' (function can be called) independently.
tommy()  # Uses and modifies Tommy's cookie's ingredients.
tommy()  # Again, but with the updated ingredients.

jenny()  # Uses and modifies Jenny's cookie's ingredients.

tommy()  # Finishes Tommy's cookie (runs out of coins).


# the statement return play_game in the parent_function is returning the play_game function itself, not the result of calling play_game. This means that when you call parent_function, it creates and returns a new function play_game that remembers the value of coins and person from the enclosing scope of parent_function.

# Here’s what happens step by step:

# parent_function is called with arguments "Tommy", 3 and "Jenny", 5, creating two closures tommy and jenny.
# Each time you call tommy() or jenny(), it executes play_game which uses and modifies the coins variable that was in scope when the closure was created.
# The nonlocal keyword allows the nested play_game function to modify the coins variable from the parent_function’s scope.
# So, when you call tommy() or jenny(), it decrements the coins by 1 and prints the current number of coins left for the respective person. When coins reaches 0, it prints that the person is out of coins.
