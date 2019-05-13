# Lesson 1
# Open a file. 
f = open('notes/raisin_team.csv')
try:
  f.read()
  # At this point, f is at the end of the file.
  # f.read() or f.readline() will always return an empty string.
  # try help(f.readline())
finally:
  f.close()
  
  
# Lesson 2
# Open a file. 
f = open('notes/raisin_team.csv')
try:
  f.read()
  f.seek(0)  #Go to first byte of file.
  print(f.readline()) 

finally:
  f.close()

# Lesson 3
with open('notes/raisin_team.csv') as f:
    line = f.readline()

# Lesson 3.1
f = open('notes/raisin_team.csv')
  line = next(f)


# Lesson 4
# Convert the contents of the file into a list line by line. 
