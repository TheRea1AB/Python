"""

This code will execute a game of Rock, Paper, Scissors !
Author: Anderson Burgess

"""
from random import randint
options = ["ROCK","PAPER","SCISSORS"]
message = {'Tie':"Yawn it's a tie",'Won':"Yay you won!",'Lost':"Aww you lost!"}

def decide_winner(user_choice,computer_choice):
  print "User choice: %s" % (user_choice)
  print "Computer choice: %s" % (computer_choice)
  if user_choice == computer_choice:
    print message['Tie']
  elif user_choice == options[0] and computer_choice == options[2]:
    print message['Won']
  elif user_choice == options[1] and computer_choice == options[0]:
    print message['Won']
  elif user_choice == options[2] and computer_choice == options[1]:
    print message['Won']
  else:
    print message['Lost']


def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice,computer_choice)
play_RPS()
