#Dictionaries
glovePrices = {'Wilson':300,'Rawlings':200,'Nike':150}
print(glovePrices)

#Prints specific key within the dictionary
print(glovePrices['Rawlings'])

#Change the value associated to a key within the dictionary
glovePrices['Wilson'] = 400
print(glovePrices['Wilson'])

#Dictionary Operations

#dictionary.keys() -- lists all the keys within the Dictionary
print(glovePrices.keys())

#dictionary.values() -- lists all the values within the dictionary
print(glovePrices.values())

#dictionary.copy() -- copies the elements in dicitonary into another Dictionary
newGlovePrices = glovePrices.copy()
print(newGlovePrices)

#Deleting a specific element within the Dictionary
del glovePrices['Wilson']
print(glovePrices)

#Clears the entire dictionary. Returns empty curly brackets
print(glovePrices.clear())


#Practice Problems

#Create a dictionary with 5 elements
videoGames = {'Call of Duty':'shooter','The Show':'Sports','God of War':'RPG','Assassins Creed':'RPG','Madden':'Sports'}
print(videoGames)

#Update the value of a key within the elements
videoGames['The Show'] = 'Baseball'
print(videoGames)

#Copy the dictionary into another dictionary and the delete the old once
newVideoGames = videoGames.copy()
print(newVideoGames)
print(videoGames.clear())
