# CONTINUE and BREAK
# continue will skip everything below and will go back to the loop
# break will jump out of the loop

# set the iterator
i = 1

# loop until i <= 20
while i <= 20:
    if i % 2 == 0:
        i += 1
        # if i is even add 1 to iterator and loop again
        continue
    elif i == 15:
        # if i == 15 jump out of the loop
        break

    print('Odd number: ', i)
    # because we jumped out of the loop we need to increase the iterator anyway
    i += 1

# end='' will cause not to force new line
print('No new line after: ', end='')
print('This is not on a new line.')
