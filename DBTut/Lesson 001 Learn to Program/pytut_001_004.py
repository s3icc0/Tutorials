# We'll provide different outputs based on age
# 1 - 18 - Important
# 21, 50, > 65 -> Important
# All others -> Not Important

# Receive age and store in variable age
# eval automatically converts number entries into Integers
age = eval(input('Enter age: '))

# Conditions:
# and : If both are true it returns true
# or : If either condition is true then true
# not : Converts a true condition into a false

# if age is both greater than or equal to 1
# and i age is less than or equal to 18 Important

""" This is fine but below it is much better
if age >= 1 and age <= 18:
    print('Important age')
"""

# the comparison here is better as it is simplified
if 1 <= age <= 18:
    print('Important age')

# if age is either 21 or 50 Important
elif age == 21 or age == 50:
    print('Important age')

# We check if age is less than 65 and then convert true to false and vice versa
# not() is used as example and the logic is also reversed < instead of >
elif not(age < 65):
    print('Important age')

# Else Not important
else:
    print('Sorry Not Important age')
