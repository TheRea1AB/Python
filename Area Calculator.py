"""

This is a simple code for calculating area
Author: Anderson Burgess

"""
print 'We are going to find the area!'
option = raw_input("Type 'C' for circle or 'T' for triangle: ")
option = option.upper()
if option == 'C':
  radius = float(raw_input('Enter radius: '))
  area = 3.14159*radius**2
  print "The area is %s" % (area)
elif option == 'T':
  base = float(raw_input('Enter the base: '))
  height = float(raw_input('Enter the height: '))
  area = .5*base*height
  print "The area of the triangle is %s" % (area)
else:
  print "Invalid Shape"

print "Program Terminated"
