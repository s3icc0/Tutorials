# ACCURATE FLOATING POINT CALCULATIONS

# decimal moodule allows more accurate calculations
# from allows to reference methods without the module reference
# Alias as D we created allows us to shorten the decimal module name

from decimal import Decimal as D


summ = D(0)
summ += D('0.1')
summ += D('0.1')
summ += D('0.1')
summ -= D('0.3')

# accurate result of the previous
print('Sum = ', summ)

# inaccurate calculation (decimal is not called)
print('.1 + .1 + .1 - .3 = ', .1 + .1 + .1 - 3)
