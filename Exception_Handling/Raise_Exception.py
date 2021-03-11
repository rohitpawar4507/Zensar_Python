# Raise Keyword -
print("Let us learn Exception")
print("Writing the code in tr..y block")

# raise keyword can be used to call a specific Except block

try:
    age = int(input("Enter the age?"))
    if age<18:
        raise ValueError
    else:
        print("The age %a is valid"%age)
except ZeroDivisionError:
    print("This is divided by zero error")

except NameError:
    print("This is name error")
except ValueError:
    print("The age %a is not valid"%age)
except:  # Handle all type of exception .
    print("The final except block...")

print('This is Demo for raise keyword')


