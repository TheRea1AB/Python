#Tuples
gradDates = (2012,2014,2016)
print(gradDates)
print(gradDates[2])

# del(gradDates) function removes the tuple entirely

#Excercises

#Write a tuple with 4 elements
seasons = ('Spring','Summer','Fall','Winter')

#Convert the tuple into a List
SEASONS = list(seasons)
print(SEASONS)

#Delete first element of the list and then make the list a tuple once more
del(SEASONS[0])
newSeasons = tuple(SEASONS)
print(newSeasons)
