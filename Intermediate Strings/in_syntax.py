"""
 - using in as Logical operator in strings
 - "in" keyword can be used to check to see if string is "in" another string
"""

fruit = "banana"
print("n" in fruit)
# outputs: True

print("m" in fruit)
# outputs: False

print("nan" in fruit)
# outputs: True

"""
 - it returns True or False and can be used in if statement
"""
if "a" in fruit:
    print("found it")
# outputs: found it
