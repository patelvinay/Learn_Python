"""
- Python string comparison is performed using the characters in both strings.
  The characters in both strings are compared one by one.
  When different characters are found then their Unicode value is compared.
  The character with lower Unicode value is considered to be smaller.
"""
word = "Banana"  # note: Uppercase B

if word < "banana":
    print("your word, " + word + " comes before banana.")
elif word > "banana":
    print("your word, " + word + " comes after banana.")
else:
    print("All right, banana.")
# outputs: your word, Banana comes before banana.
