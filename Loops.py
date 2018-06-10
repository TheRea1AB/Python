#Loops
# Def: Executes while some statement is true

#For Loop
Sports = ['Baseball','Football',"Basketball"]
for sport in Sports:
    print(sport)

# range function allows for outputs to be sequencial
# end = ' ' ; This statement prints the output on one line
for number in range(1,11):
    print(number, end=" ")

# This statement inputs indent within the code
print()
print()


#while Loop
#Outputs The number is 10-20
number2 = 10
while number2 >= 10 and number2 <= 20:
    print("The number is: {}".format(number2))
    number2 = number2 + 1


#Nested Loop
num = 1
for col in range(1,4):
    for row in range(1,4):
        print(num,end='')
    num = num + 1
    print()

#Break: Stops the Loop
for number3 in range(1,6):
    if number3 == 3:
        break
    else:
        print(number3,end=' ')

print()
print()

#Continue: Excutes the entire loop; skips certain iterations
for number3 in range(1,6):
    if number3 == 3:
        continue
    else:
        print(number3,end=' ')

print()
print()

#Else: Excutes only if the break statement does not execute


for num2 in range(1,20):
    if num2 == 15:
        print("There was a break at {}".format(num2))
        break
    else:
        print(num2)
else:
    print('There was no break!')

#Excercise Problems
#Write a program to print numbers 1 - 10

print()
print()

number5 = 1
while number5 >= 1 and number5 <= 10:
    print(number5, end=' ')
    number5 = number5 + 1

print()
print()

#Write a program to print the sum of all the odd numbers from 1-10
number6 = 0
for num in range(1,11):
    if num % 2 is not 0:
        number6 = num + number6
print(number6)


print()
print()

#Write a program that checks to see if a number is prime or not

print("Enter a postive number greater than 2: ")
num2 = input()
num2 = abs(int(num2))
for prime in range(2,num2):
    if prime % 2 is 0:
        print('This number is not prime')
        break
else:
    print('This number is prime!')
