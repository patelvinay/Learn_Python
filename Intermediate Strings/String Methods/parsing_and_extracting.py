"""
Parsing and Extracting
- finding host name from email data
"""
data = "pinbot@info.pinterest.com Sat, Jan 22, 4:35 AM (12 days ago)"
at_position = data.find("@")
print(at_position)

space_position = data.find(" ", at_position)
print(space_position)

hostname = data[at_position + 1: space_position]
print(hostname)
