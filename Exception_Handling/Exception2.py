#finally block
'''
try
except
finally
first except block execute and then finally executed
'''
try:
    print('Inside try block ')
    try:

        a = int(input('Enter no :'))
        b = int(input('Enter b :'))
        c = a / b
        print('a/b=%d' % c)
    except NameError:
        print('Except for inner try ')
    finally:  # it will exceute no matter error hai ya nahi hai AS many try those many finally can take
        print('Inner Finally Block -Executed')


except ZeroDivisionError:
    print('Inside Except Block for ZeroDivisionError of outer try')
    print('The value of b cannot be zero')
except NameError:
    print('Inside except block for NameError for outer try' )
    print('Some variable may not definied ')
except:  # handle another exception other than above 3
    print('Inside except block for all other Exception for outer try')
finally:
    print('THIS IS OUTER FINALLY BLOCK ')

print('Code Complete')