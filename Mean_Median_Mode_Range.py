
print('Enter Number 1')
num1 = int(input())
print('Enter Number 2')
num2 = int(input())
print('Enter Number 3')
num3 = int(input())
print('Enter Number 4')
num4 = int(input())
print('Enter Number 5')
num5 = int(input())

numbers = [num1,num2,num3,num4,num5]
numbers.sort()
print(numbers)

#Mean
mean = (num1+num2+num3+num4+num5)/5
print('Mean: {}'.format(mean))

#Median
print('Median: {}'.format(numbers[2]))

#Range
range = numbers[4] - numbers[0]
print('Range: {}'.format(range))

#Mode
