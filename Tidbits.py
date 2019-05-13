# Everything in Python is an object.
# type(3)
# <class 'int'>
# type(int)
# <class 'type'>
# type(type)
# <class 'type'>


# In Py, we have 4 different quoting symbols:
# ' " ''' """

# __ is called dunder. [Double underscore]

person = 'Julie'
type(person)

dir()

# Lists all the methods available. 
dir(person) 

# A file that ends with .py becomes a module.

# Tells you what the object is, what it does.
help(str)

# The following is the same as:
'1' + '1' + '1' + '1' 
# '1111'
# is the same as below:

'1' * 4

# For loop: 
# As soon as you start the for loop -> an iterator class is invoked. this saves the states.
for i in range(5):
  print('hi')

# String that moves to the right every time it prints.
a = 'It moves to the right!'
b = ' '
for i in range(5):
    print(b + a)
    b = b + ' '

# understanding reference counters.

Ilin = Person('Ilin')
Ayesha = Person('Ayesha')
Sindhu = Person('Sindhu')

# All person objects have 1 reference counters each.

Ilin = Sindhu

# Now Ilin is a tag to the Person object of Sindhu. So, Person('Sindhu') has 2 reference counters.
# And, Person('Ilin') has 0 reference counters.

# Person('Ilin') is eligible for garbarge collection.

# None is a singleton object.
# At any point there will only be one object in memory. 
None
id(None)
hex(id(None))

