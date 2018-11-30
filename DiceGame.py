"""Welcome to the Game! Guess the number!"""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Enter a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides*2
  print "The maximum possible value is %d" % (max_val)
  guess = get_user_guess()
  
  if guess > number_of_sides*2 or guess < 1:
    print 'Invalid!'
  else:
    print 'Rolling...'
    sleep(2)
    print "Roll One: %d" % (first_roll)
    sleep(1)
    print "Roll Two: %d" % (second_roll)
    sleep(2)
    total_roll = first_roll + second_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "Winner! Winner! Chicken Dinner!"
    else:
      print ":/"
    
roll_dice(6)
