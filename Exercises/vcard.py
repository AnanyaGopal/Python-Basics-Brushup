''' Real life, old example of Python
    featuring CSV files, HTML generation,
    file handling, templating, and other
    core skills
'''
import urllib.parse.urlencode


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

'''


filename = '%s_%s.vcf' % (fname, lname)
with open(filename, 'w') as vcard_file:
    vcard_file.write(vcard)








line = line.rstrip()
fields = line.split(',')
lname = fields[0]
fname = fields[1]
'''
'''
%s %d -> Interpolation
%s ->  placeholders.
% (args1, args2) --> GROUPING
'''
##


