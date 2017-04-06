# Print odds from 1 to 20

# cycle i in range of 1-20
for i in range(1, 21):
    # i is not an even number
    if i % 2 != 0:
        print('{} is an odd number'.format(i))
