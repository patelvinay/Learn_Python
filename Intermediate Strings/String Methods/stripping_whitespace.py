"""
    lstrip() and rstrip() removes whitespace at the left or right
"""

greet = "   Hello John    "
print(greet.lstrip())
# outputs: 'Hello John    '

print(greet.rstrip())
# outputs: '   Hello John'

"""
strip() removes both beginning and ending whitespace
"""
print(greet.strip())
# outputs: 'Hello John'
