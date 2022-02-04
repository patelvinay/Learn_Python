"""
    the newline character
    - we use a special characters called the "newline" to indicate when a line ends
    - we represent it as \n in strings
    - newline is still one character - not two
"""

file = "Hello\nWorld!"
print(file)
# Hello
# World!

file = "X\nY"
print(file)
# X
# Y

print(len(file))
# 3
