#ExceptionHandling-
'''
1.Exception -abnormal condition in program resulting in disruption in the flow of program
--Zerodivisioin error-occur when num divide by zero
--Name Error -occur when name not found


'''
print('Let us learn Exception ')
#First code
'''try:
    print('Inside try block ')
    a = int(input('Enter no :'))
    b = int(input('Enter b :'))  # if i give space and then write b=... then give IndentationError: unexpected indent
    c = a / b  # if just write a/b it give NameError: name 'c' is not defined
    print('a/b=%d'%c)
except:
    print('Inside Except Block ')
    print('The value of b cannot be zero')
print('Code is completed ')'''


'''try:
    print('Inside try block ')
    a = int(input('Enter no :'))
    b = int(input('Enter b :'))
    # b = int(input('Enter b :')) if give space give IndentationError: unexpected indent
    c = a / b
    print('a/b=%d'%c)
except:
    print('Inside Except Block ') #if give space give IndentationError: unexpected indent
    print('The value of b cannot be zero')
finally:
    print('Code is completed ')'''

#if indentation error then it will not go in try or except block but we cannot handle indentation error

#multiple try except
#at time it will execute one except block only
'''means if we does not definied c and also give value of b zero 
   then also it will execute onle ZeroDivisionError except block
   because in program i have write ZeroDivisionError bexcpt block 1st
   and then NameError except block'''

try:
    print('Inside try block ')
    a = int(input('Enter no :'))
    b = int(input('Enter b :'))
    c=a/b
    print('a/b=%d'%c)
except IndentationError:
    print('Inside except block for IndentationError ')
except ZeroDivisionError:
    print('Inside Except Block ')
    print('The value of b cannot be zero')
except NameError:
    print('Inside except block for NameError ')
    print('Some variable may not definied ')
except :#handle another exception other than above 3
    print('Inside except block for all other Exception ')

print('Code Complete')