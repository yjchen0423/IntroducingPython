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


