"""Ch. 08"""

"""Ch. 8.1"""

'fileobj = open(filename, mode)'

'1st character of mode: '
'r(read), w(write, create if not exist), x(write only if file not exist), a(write after the end)'

'2nd character of mode: '
't(type), b(binary)'


"""Ch. 8.1.1"""

poem = """
There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.
"""

print(len(poem))

fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

# fout = open('relativity', 'wt')
# size = len(poem)
# offset = 0
# chunk = 100
# while True:
#     if offset > size:
#         break
#     fout.write(poem[offset:offset+chunk])
#     offset += chunk
#
#
# fout.close()


"""Ch. 8.1.2"""
fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))


poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
print(len(poem))


poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line

fin.close()
print(len(poem))


poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line

fin.close()
print(len(poem))


fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')

for line in lines:
    print(line, end='')


"""Ch. 8.1.3"""

bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile', 'wb')
print(fout.write(bdata))
fout.close()


fout = open('relativity', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk

fout.close()


"""Ch. 8.1.4"""
fin = open('bfile', 'rb')
bdata = fin.read()
print(len(bdata))

fin.close()


"""Ch. 8.1.5"""

"""with expression as variable"""

with open('relativity', 'wt') as fout:
    fout.write(poem)


"""Ch. 8.1.6"""

'seek()'

fin = open('bfile', 'rb')
print(fin.tell())


print(fin.seek(255))


bdata = fin.read()  # fin will start at position 255
print(len(bdata))  # there is only one character in bdata

print(bdata[0])

fin = open('bfile', 'rb')

print(fin.seek(-1, 2))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])

fin = open('bfile', 'rb')
print(fin.seek(254, 0))
print(fin.tell())

print(fin.seek(1, 1))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])



"""Ch. 8.2.1"""

'reading csv'



import csv

villains =[
    ['Doctor', 'No'],['Rosa', 'Klebb'],['Mister', 'Big'],['Auric', 'Goldfinger'],['Ernst', 'Blofeld'],
]

with open('villains', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

import csv
with open('villains', 'rt') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]

print(villains)

import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

print(villains)


'DictWriter(), writeheader()'

import csv
villains =[
    {'first': 'Doctor', 'last': 'No'},{'first': 'Rosa', 'last': 'Klebb'}, {'first': 'Mister', 'last': 'Big'}, {'first': 'Auric', 'last': 'Goldfinger'}, {'first': 'Ernst', 'last': 'Blofeld'},
]

with open('villains', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)


import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

print(villains)


"""Ch. 8.2.2"""

'XML'

import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')

root = tree.getroot()
print(root.tag)

for child in root:
    print('tag: ', child.tag, 'attribute:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes: ', grandchild.attrib)

print(len(root))  # number of menu orders: 3, breakfast, lunch, and dinner
print(len(root[0]))  # number of breakfast items


"""Ch. 8.2.4"""

'dump()'

menu = \
{
    "breakfast": {
        "hours": "7-11",
        "items": {
            "breakfast burritos": "$6.00",
            "pancakes": "$4.00"
            }
        },
    "lunch": {

        "hours": "11-3",
        "items": {
            "hamburger": "$5.00"
            }
        },
    "dinner": {
        "hours": "3-10",
        "items": {
            "spaghetti": "$8.00"
        }
    }
}

'dump() - encode to json string'

import json
menu_json = json.dumps(menu)
print(menu_json)


'loads() - convert json string to Python'
menu2 = json.loads(menu_json)
print(menu2)


"""Ch. 8.2.5"""
'YAML'

import yaml

with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()

data = yaml.load(text)

print(data['details'])
print(len(data['poems']))


"""Ch. 8.2.7"""

'configparser'

import configparser
cfg = configparser.ConfigParser()
print(cfg.read('settings.cfg'))

print(cfg['french'])
print(cfg['french']['greeting'])
print(cfg['files']['bin'])


"""Ch. 8.4"""
'SQL - Structured Query Language'


'DDL - Data Definition Language'
'DML - Data Manipulation Language'

'DB - API'
'connect()'
'cursor()'
'execute() & executemany()'
'fetchone(), fetchmany(), fetchall()'

import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
# curs.execute('''CREATE TABLE zoo
# (critter VARCHAR(20) PRIMARY KEY,
# count INT,
# damages FLOAT)''')

curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')

'placeholder'
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))

curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

curs.execute('SELECT * FROM zoo ORDER BY count')
print(curs.fetchall())

curs.execute('SELECT * FROM zoo ORDER BY count DESC')
print(curs.fetchall())

curs.execute('''SELECT * FROM zoo WHERE
                damages = (SELECT MAX(damages) FROM zoo)''')
print(curs.fetchall())

curs.close()
conn.close()


"""Ch. 8.4.6"""
'SQLAlchemy'

import sqlalchemy as sa

conn = sa.create_engine('sqlite://')

conn.execute("""CREATE TABLE zoo2
                (critter VARCHAR(20) PRIMARY KEY,
                 count INT,
                 damages FLOAT)""")

ins = 'INSERT INTO zoo2 (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)

rows = conn.execute('SELECT * FROM zoo2')

print(rows)

for row in rows:
    print(row)



"""Ch. 8.5"""
'NoSQL - not only SQL'


"""Ch. 8.5.1"""
'dbm family'

import dbm
db = dbm.open('definitions', 'c')
db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'

print(len(db))
print(db['pesto'])

db.close()

db = dbm.open('definitions', 'r')
print(db['mustard'])


"""Ch. 8.7 Exercise"""

# 1.
test1 = "This is a test of the emergency test system"
fout = open('test.txt', 'wt')
fout.write(test1)
fout.close()

# 2.
fin = open('test.txt', 'rt')
test2 = fin.read()
print(test1)
print(test2)

# 3.
books = """authors,book
J R R Tolkien,The Hobbit
Lynne Truss,\"Eats, Shoots & Leaves\""""

fout = open('books.csv', 'wt')
fout.write(books)
fout.close()

# 4.
import csv

with open('books.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    books_csv = [row for row in cin]

print(books_csv)

# 5.
books2 = """title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
"""

with open('books2.csv', 'wt') as fout:
    fout.write(books2)

# 6.
import sqlite3
conn = sqlite3.connect("books.db")
curs = conn.cursor()
# curs.execute('''CREATE TABLE book
# (title VARCHAR(50) PRIMARY KEY,
# author VARCHAR(50),
# year INT)''')
# curs.execute('''DROP TABLE book''')

# 7.
import sqlite3
import csv
ins = 'INSERT INTO book (title, author, year) VALUES(?, ?, ?)'
with open('books2.csv', 'rt') as fin:
    books = csv.DictReader(fin)
    for book in books:
        curs.execute(ins, (book['title'], book['author'], book['year']))

rows = conn.execute('SELECT * FROM book')
for row in rows:
    print(row)


# 8.
print("------")
titles = conn.execute('SELECT title FROM book ORDER BY title')
for title in titles:
    print(title[0])

# 9.
print("------")
order_by_year = conn.execute('SELECT * FROM book ORDER BY year')
for order in order_by_year:
    print(*order, sep=',')

# 10.
print("10------")

import sqlalchemy as sa
conn = sa.create_engine('sqlite:///books.db')
rows2 = conn.execute('SELECT title FROM book ORDER BY title')
print(rows2)

