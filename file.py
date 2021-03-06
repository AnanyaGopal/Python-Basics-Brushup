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
f.close()

# Lesson 4
# Convert the contents of the file into a list line by line. 

f = open('notes/raisin_team.csv')
file_elements = list(f)
print(file_elements)
# line = next(f)
f.close()


# Lesson 5
# Open a list of csv, put info in a file.
''' Real life, old example of Python
    featuring CSV files, HTML generation,
    file handling, templating, and other
    core skills
'''
vcard_format = '''
BEGIN:VCARD
VERSION:2.1
N:%s;%s 
FN:%s %s
TITLE: %s
TEL;WORK;VOICE: %s
EMAIL: %s
REV:20080424T195243Z
END:VCARD
'''

f = open('notes/raisin_team.csv')

line = next(f)
line = line.rstrip()
fields = line.split(',')
lname = fields[0]
fname = fields[1]
designation = fields[2]
email = fields[3]
phone = fields[4]

print(fields)

vcard = vcard_format % (fname, lname, lname, fname, designation,email, phone)
print(vcard)

filename = '%s_%s.vcf' % (fname, lname)
with open(filename, 'w') as vcard_file:
    vcard_file.write(vcard)
