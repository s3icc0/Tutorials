# floats are not precise
i = 0.1 + 0.1 + 0.1 - 0.3
print(i)

# floats prints nonsense after 16 digits
i = .11111111111111111111111111111111
j = .00000000000000001000000000000001
print('Answer: {:.32}'.format(i + j))

# Order of operations
# Seems like in math to me
print('3 + 4 * 5 = {}'.format(3 + 4 * 5))
print('(3 + 4) * 5 = {}'.format((3 + 4) * 5))
