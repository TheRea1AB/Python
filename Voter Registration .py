"""Voter Registration"""
print ("Welcome to Votor Registration!")
print ("In order to be eligible to vote, you must be at least 18 years old and a U.S Citizen")
# Array of all state abbreviations
us_states = ['AL', 'AK', 'AZ', 'AR','CA', 'CO','CT', 'DE','DC', 'FL',
             'GA', 'HI', 'ID', 'IL','IN', 'IA','KS', 'KY','LA', 'ME',
             'MD', 'MA', 'MI', 'MN','MS', 'MO','MT', 'NE','NV', 'NH',
             'NJ', 'NM', 'NY', 'NC','ND', 'OH','OK', 'OR','PA', 'RI',
             'SC', 'SD', 'TN', 'TX','UT', 'VT','VA', 'WA','WV', 'WI', 'WY']

# Prompt for citizenship
print ("> Are you a U.S citizen? (Enter 'Y' for yes, 'N' for no)")
IS_VALID_CITIZEN = False
while IS_VALID_CITIZEN is False:
    citizen = input()
    if str(citizen) == 'Y' or str(citizen) == 'y':
        IS_VALID_CITIZEN  = True
    elif str(citizen) == 'N' or str(citizen) == 'n':
        print ("> Sorry, only U.S citizens are eligible to vote.")
        print ("> So you'll say yes this time, right:")
    else:
        print ("> You must have misclicked... that's 'Y' for yes and 'N' for no")
        print ("> Please enter your response:")

# Prompt for age
print ("> How old are you?")
IS_VALID_AGE = False
while IS_VALID_AGE is False:
    age = input()
    if int(age) < 18:
        print ("> Sorry, you are to young to vote")
        print ("> You could just fake your age like the rest of us... try another one:")
    elif int(age) > 120:
        print ("> You are " + age + " years old?! Try again in the next life.")
        print ("> Did you have another age in mind... maybe?")
    else:
        print("> Great! Just need a little more information to verify your voter eligibilty")
        IS_VALID_AGE = True

# Prompt for state
print("> Where do you live? (U.S Territories ONLY)")
print("> Enter state acronym (e.g Maryland -> MD)")
IS_VALID_STATE = False
while IS_VALID_STATE is False:
    app_state = input()
    if app_state in us_states:
        IS_VALID_STATE = True
    else:
        print("> Not a valid state. Try another:")

# Prompt for zip code
print("> What is your zip code?")
IS_VALID_ZIP = False
while IS_VALID_ZIP is False:
    zip = input()
    if zip.isnumeric() and int(zip) > 9999 and int(zip) <= 99999:
        IS_VALID_ZIP = True
    else:
        print("> Invalid Zip Code. Try another:")

# Prompt for name...
print ("> What is your first name?")
FIRST_NAME = str(input())
print ("> What is your last name?")
LAST_NAME = str(input())

# and print final message!
print(f'> Congratulations {FIRST_NAME} {LAST_NAME}! You are eligible to vote.')
