# Add each character, and it's ordinal, of user's text input, to two lists
s = input("Enter value: ")  # this line requires Python 3.x, use raw_input() instead of input() in Python 2.x
l1 = []
l2 = []
for c in s:   # in Python, a string is just a sequence, so we can iterate over it!
    l1.append(c)
    l2.append(ord(c))
print(l1)
print(l2)
