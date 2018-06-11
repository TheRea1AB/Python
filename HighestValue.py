# Which of the two numbers is greater
def greatestNumber(Number1,Number2):
    if Number1 > Number2:
        print('Number 1 is the bigger number')
        return Number1
    elif Number2 > Number1:
        print('Number 2 is the bigger number')
        return Number2
    else:
        print('These two numbers are the same')
        return Number1

print('Enter Number 1: ')
Number1 = int(input())
print('Enter Number 2: ')
Number2 = int(input())

maxNumber = greatestNumber(Number1,Number2)
print("The maximum is = {}".format(maxNumber))
