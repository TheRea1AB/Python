# Practice with Lists
favoriteFruits = ['apple','orange','banana']

#returns the entire list
print(favoriteFruits)

#returns the specific object in that particular index
print(favoriteFruits[2])

#replace objects within the list manually
favoriteFruits[1] = 'pear'
print(favoriteFruits)


#List Operations

#adds a new object to the back of the list
favoriteFruits.append('kiwi')
print(favoriteFruits)

#adds a new object to a specific index within the list
favoriteFruits.insert(1,'pineapple')
print(favoriteFruits)

#removes an object from a list
favoriteFruits.remove('apple')
print(favoriteFruits)

#places objects within the list in alphabetical or numerical order
favoriteFruits.sort()
print(favoriteFruits)

#reverse the elements within the list
favoriteFruits.reverse()
print(favoriteFruits)

# Outputs the last element in the list and then removes it from the list forever
print(favoriteFruits.pop())
print(favoriteFruits)


#Practice Problems
#Excercise 1
sports = ['baseball','football','basketball','tennis','soccer']
print(sports)

#Excercise 2
sports[2] = 'lacrosse'
print(sports)

#Excercise 3
equipment = ['ball','stick','helmet']
print(sports + equipment)
