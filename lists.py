# Lists are data structures that hold any object.
# Notice that Lists don't actually hold the data -> They hold the refernces to the data objects.
# You can append any kind of objects to it using list.append() funtion, one obj at a time.
l = [1,2,3]

l.append(0.5)
l.append(print)
l.append(NameError)

# Getting the element of the lists.
# l[0], l[1]


# Slicing
# Below statement will give you 5 elements - 0th to the 4th.
l[0:5] 

# Sizeable
# If len(object) works, then it is not sizeable.
'''
len(tuple)
len(list)

>>> len(5)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    len(5)
TypeError: object of type 'int' has no len()
>>> len(True)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    len(True)
TypeError: object of type 'bool' has no len()
>>> len(print)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    len(print)
TypeError: object of type 'builtin_function_or_method' has no len()
'''

# Indexable

# If the object is Indexable and Sizeable -> it is iterable.

