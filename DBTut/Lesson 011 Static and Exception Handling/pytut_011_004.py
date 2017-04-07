try:
    alist = [1, 2, 3]

    # index 3 does not exist therefore will raise error
    print(alist[3])


# except(IndexError, NameError):
#     print('Multiple errors handled here')

except IndexError:
    print('Sorry that index does not exist.')

except:
    print('An unknown error occured.')
