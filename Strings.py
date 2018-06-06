#Practice with Strings

Sport = 'Baseball'
Name = 'Anderson'
Food = 'Pizza'
print(Sport)
print(Name)
print(Food)

print(Sport[2])
print(Sport[-1])

print("The Real AB's Macbook")
# Double quotations can be used in strings
# This allows you to use a single quotation within the string if necessary


#strings can be changed
Sport = 'Football'
print(Sport)


#String Operations
string = "My name is Anderson Burgess and I love baseball"
string.upper()  # characters are now all UPPERCASE
print(string)

string.lower()  # characters are now all lowercase
print(string)

string.replace('baseball','programming') #replace words within a string
print(string)

# Allows for slicing; Specific parts of the string
print(string[11:27])

len(string)   # Length function returns the number of characters within the string
print(len(string))
#String Formatting
example = 'and programming.'
print("My name is Anderson Burgess and I love baseball {}".format(example))
