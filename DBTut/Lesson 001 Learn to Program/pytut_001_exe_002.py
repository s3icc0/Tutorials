# If age is 5 Go to Kindergarten
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater then 17 say go to college
# Try to complete with 10 or less lines

# Input age
# Convert age to Integer
age = eval(input('Enter age: '))

# Evaluate age and print correct result
if age == 5:
    print('Go to Kindergarten')
elif 6 <= age <= 17:
    # as the distance is always 5 we can assign class linearly
    grade = age - 5
    # added to handle 1st
    if grade == 1:
        print('Go to {}st grade'.format(grade))
    # added to handle 2nd
    elif grade == 2:
        print('Go to {}nd grade'.format(grade))
    elif grade == 3:
        print('Go to {}rd grade'.format(grade))
    else:
        print('Go to {}th grade'.format(grade))
elif age > 17:
    print('Go to college')
else:
    print('Sorry, you are to young to be terrorized by the educational system')
