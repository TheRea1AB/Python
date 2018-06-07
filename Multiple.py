#Check to see if a number is a multiple of 3
#Check to see if that samne number is a multple of 7

#Ask the user for input; Use the input function
print('Enter a number: ')

# int converts the users input from a string to an integer so that there's no error
number = int(input())
if number % 3 is 0 or number % 7 is 0:
    if number % 7 is 0 and number % 3 is 0:
        print('The number is a multiple of 3 and 7.')
    elif number % 7 is 0:
        print('The number is a multiple of 7, but not 3.')
    else:
        if number % 3 is 0:
            print('The number is multiple of 3, but not 7.')
else:
    print('The number is neither a multiple of 3 or 7.')
