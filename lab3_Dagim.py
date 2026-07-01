# Dagim/ Lab 3/ Intro to python

# PREDICT:
# I think my handle has 5 characters.
# Ticket 1
username = "Dagim"

# Print the length of the handle
print(len(username))

# EXPLAIN:
# Yes, len() counts every character in the string,
# including symbols such as @ and with letters and numbers.

# PREDICT:
# I think it will be D and M
# Ticket 2
username = "Dagim"

print(username[0])                  # first character
print(username[len(username) - 1])  # last character
# EXPLAIN:
# Because python starts counting from 0
# Ticket 3
username = "Dagim"

print("Welcome to Loop, @" + username + "!")
print(f"Welcome to Loop, @{username}!")
# PREDICT
# It will look the same 
# EXPLAIN
# I think the f string is easier because it is cleaner and easier to understand
# Ticket 4
username[0] = "X" # run this, it breaks on purpose
# Type Error 'str' object does not support item assignment 