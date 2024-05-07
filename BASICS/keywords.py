# --------------------------
# -- KEYWORDS --
# --------------------------
# [not]: return opposite value
# [and]: return TRUE only when 2 values ARE True
# [or]: return TRUE when 1 of the value IS True
# --------------------------

x = True
y = False
z = True

# not
print(x)  # True
print(not x)  # False

# and
print(x and y)  # False : x = True, y = False
print(x and z)  # True : x = True, z = True
print(y and x)  # False : y = False, x = True
print(y and y)  # False : y = False, y = False
print(y and z)  # False : y = False, z = True
print(z and x)  # True : z = True, x = True
print(z and y)  # False : z = True, y = False
print(z and z)  # True : z = True, z = True

# or
print(x or y)  # True : x = True, y = False
print(x or z)  # True : x = True, z = True
print(y or x)  # True : y = False, x = True
print(y or y)  # False : y = False, y = False
print(y or z)  # True : y = False, z = True
print(z or x)  # True : z = True, x = True
print(z or y)  # True : z = True, y = False
print(z or z)  # True : z = True, z = True
