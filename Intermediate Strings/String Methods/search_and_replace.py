"""
 - replace() function is like a "search and replace" operation in a word processor
 - its replaces all occurrences of the search string with the replacement string
"""

greet = "Hello John"
replace_name = greet.replace("John", "Bob")
print(replace_name)
# outputs: Hello Bob

replace_name = greet.replace("o", "x")
print(replace_name)
# outputs: Hellx Jxhn
