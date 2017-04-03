# ------------------------------------------------------------------------------
# READ THE FILE

""" # The bad way
f = open('000 Nav.txt')
text = f.read()
for line in text.split('\n'):
    print(line)
f.close()
"""

""" # The little better way
f = open('000 Nav.txt')
for line in f:
    print(line)
f.close()
"""

# The good way - Pythonic way

with open('000 Nav.txt') as f:
    for line in f:
        print(line)
