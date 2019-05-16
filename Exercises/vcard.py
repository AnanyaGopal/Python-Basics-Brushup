''' Real-life, old example of Python
    featuring CSV files, HTML generation,
    file handling, templating, and other core skills
'''
vcard_template = '''\
BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s %s
ORG:Raisins R Us, Inc.
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK;PREF:;;100 Flat Grape Dr;Fresno;CA;95555;United States of America
EMAIL:%s
REV:20080424T195243Z
END:VCARD
'''

f = open('../notes/raisin_team.csv')
for line in f:
    line = line.rstrip()
    fields = line.split(',')
    lname = fields[0]
    fname = fields[1]
    title = fields[2]
    email = fields[3]
    phone = fields[4]

    vcard = vcard_template % (fname, lname, lname, fname, title, phone, email) 
    print(vcard)

    filename = '%s_%s.vcf' % (fname, lname)
    with open(filename, 'w') as vcard_file:
        vcard_file.write(vcard)

    import urllib.parse

    root_url = 'https://chart.googleapis.com/chart?'
    query = dict(cht='qr', chs='300x300', chl=vcard)
    url = root_url + urllib.parse.urlencode(query)
    print(url)

    import urllib.request
    with urllib.request.urlopen(url) as u:
        image = u.read()

    filename = '%s_%s.png' % (fname, lname)
    with open(filename, 'wb') as image_file:
            image_file.write(image)
