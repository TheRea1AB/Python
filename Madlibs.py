"""
A simple Mad Libs Code
Author: Anderson Burgess
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world." 

print 'The Mad Libs Story has begun...'
# Asks the user for a name
name = raw_input('Enter a name: ')

# Asks the user for 3 adjactives
adj1 = raw_input('Adjective 1: ')
adj2 = raw_input('Adjective 2: ')
adj3 = raw_input('Adjective 3: ')

# Asks the user for a verb
verb = raw_input('Enter a verb: ')

# Asks the user for 2 nouns
noun1 = raw_input('Noun 1: ')
noun2 = raw_input('Noun 2: ')

# More inputs for the user
animal = raw_input('Animal: ')
food = raw_input('Food: ')
fruit = raw_input('Fruit: ')
superhero = raw_input('Superhero: ')
country = raw_input('Country: ')
dessert = raw_input('Dessert: ')
year = raw_input('Year: ')

print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2)
