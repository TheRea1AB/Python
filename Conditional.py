#Conditional Statements

#if statement
grade = 95
if grade > 90:
    print("You got an A!")

#if-else statement
grade = 75
if grade > 90:
    print('You got an A')
else:
    print('You did not get an A')

#if-elif statement
grade = 85
if grade > 90:
    print("A")
elif grade > 80:
    print("B")
else:
    print("Youg did not get an A or B")

#nested statement
grade = 100
if grade > 90:
    if grade == 100:
        print("Perfect!")

#Operations

#AND
grade = 85
if grade < 90 and grade >= 80:
    print('You get a B')
else:
    print('You did not get a B')

#OR
sport = 'Baseball'
if sport is 'Football' or sport is 'Baseball':
    print("The Greatest Game in the World!")



#Excercices
#Write a program that checks to see if a number is less than 10

number = 5
if number < 10:
    print("Number is less than 10")

number = 87
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

number = 200
if number % 50 == 0 and number % 10 == 0:
    if number % 30 == 0:
        print('Number is divisible by 10, 30, and 50')
    else:
        print('Number is divisible by 10 and 50 but not 30')
