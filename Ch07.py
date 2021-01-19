"""Ch. 7.1.1"""

'unicode'

def unidoce_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f'value = {value}, name = {name}, value2 = {value2}')

unidoce_test('A')
unidoce_test('S')
unidoce_test('$')
unidoce_test('\u20ac')
unidoce_test('\u2603')


snowman = '\u2603'
print(len(snowman))
ds = snowman.encode('utf-8')
print(len(ds))

place = 'caf\u00e9'
print(place)

place_bytes = place.encode('utf-8')
print(place_bytes)


"""Ch. 7.1.2"""

'formatting'

"""
----old----
%s string
%d decimal integer
%x hex integer
%o octal integer
%f decimal float
%e exponential float
%g decimal or exponential float
%% a %
"""

print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)

print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)

print('%d%%' % 100)

actor = 'Max'
cat = 'Che'
weight = 28

print("My wife's favorite actor is %s" % actor)
print("our cat's name is %s and her weight is %d pounds." % (cat, weight))

n = 42
f = 7.03
s = 'string cheese'


print("%d %f %s" % (n, f, s))
print("%10d %10f %10s" % (n, f, s))
print("%-10d %-10f %-10s" % (n, f, s))
print("%10.4d %10.4f %10.4s" % (n, f, s))
print("%.4d %.4f %.4s" % (n, f, s))
print("%*.*d %*.*f %*.*s" % (10, 4, n, 10, 4, f, 10, 4, s))


"""
----new----

"""

print("{} {} {}".format(n, f, s))
print("{2} {0} {1}".format(n, f, s))
print("{n} {f} {s}".format(n = 42, f = 7.03, s = 'string cheese'))

d = {'n':42, 'f':7.03, 's':'string cheese'}
print("{0[n]} {0[f]} {0[s]} {1}".format(d, 'other'))

print("{0:d} {1:f} {2:s}".format(n, f, s))

print("{n:d} {f:f} {s:s}".format(n=42, f=7.03, s='string cheese'))

print("{0:10d} {1:10f} {2:10s}".format(n, f, s))

# right
print("{0:>10d} {1:>10f} {2:>10s}".format(n, f, s))

# left
print("{0:<10d} {1:<10f} {2:<10s}".format(n, f, s))

# center
print("{0:^10d} {1:^10f} {2:^10s}".format(n, f, s))


print("{0:^10d} {1:^10.2f} {2:^10.4s}".format(n, f, s))

# there are total 20 chars and BIG SALE is in center
print('{0:!^20s}'.format('BIG SALE'))


"""Ch. 7.1.3"""

'Regular Expression'
're module'
'match()'
# match('pattern', 'source')


import re
source = 'Young Frank'

m = re.match('You', source)
if m:
    print(m.group())
    # all matches are returned as m.group()

m = re.match('^You', source)
if m:
    print(m.group())

m = re.match('Frank', source)
if m:
    print(m.group())
else:
    print('Not found!')

m = re.match('.*Frank', source)
if m:
    print(m.group())
    # . means any single character
    # * means zero or more of the preceding thing
    # .* means any number of characters

m = re.search('Frank', source)
if m:
    print(m.group())

'findall() - return all matched results'
m = re.findall('n', source)
print(m)
print(f"Found {len(m)} matches")

m = re.findall('n.?', source)
print(m)
# .? means zero or one of any single character

'split() - split by pattern'
m = re.split('n', source)
print(m)

'sub("pattern1", "pattern2", source) - replace "pattern1" with "pattern2" in source'
m = re.sub('n', '?', source)
print(m)


'special characters'
"""
\d      a single digit
\D      a single non-digit
\w      a alphanumeric character
\W      a non-alphanumeric character
\s      A whitespace character
\S      A non-whitespace character
\b      A word boundary
\B      A non-word boundary
"""

import string
printable = string.printable

print(len(printable))
print(printable[:50])
print(printable[50:])

print(re.findall('\d', printable))
print(re.findall('\w', printable))

print(re.findall('\s', printable))


x = 'abc' + '-/*' + '\u00ea' + '\u0115'

print(re.findall('\w', x))


'pattern specifiers'


"""
abc             literal abc
(expr)          expr
expr1|expr2     expr1 or expr2
.               any character expect \n
^               start of source string
$               end of source string
prev?           zero or one prev
prev*           zero or more prev, as many as possible
prev*?          zero or more prev, as few as possible
prev+           one or more prev, as many as possible
prev+?          one or more prev, as few as possible
prev{m}         m consecutive prev
prev{m,n}       m to n consecutive prev, as many as possible
prev{m,n}?      m to n consecutive prev, as few as possible
[abc]           a or b or c
[^abc]          not (a or b or c)
prev(?=next)    prev if followed by next
prev(?!next)    prev if not followed by next
(?<=prev)next   next if preceded by prev
(?<!prev)next   next if not preceded by prev
"""

source = """I wish I may, I wish I might
            Have a dish of fish tonight."""

print(re.findall('wish', source))
print(re.findall('wish|fish', source))
print(re.findall('^wish', source))
print(re.findall('^I wish', source))
print(re.findall('fish$', source))
print(re.findall('fish tonight.$', source))
print(re.findall('fish tonight\.$', source))

print(re.findall('[wf]ish]', source))
print(re.findall('[wsh]+]', source))
print(re.findall('ght\W', source))

print(re.findall('I (?=wish)', source))
print(re.findall('(?<=I) wish', source))

print(re.findall(r'\bfish', source)) # add r so that \b means a word boundary
print(re.findall(r'fish', source))

m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))



"""Ch. 7.2"""

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)

the_byte_array = bytearray(blist)
print(the_byte_array)

# the following code will be error as bytes are not changeable
# the_bytes[1] = 127


the_byte_array[1] = 127
print(the_byte_array)


the_bytes = bytes(range(0, 255))
the_byte_array = bytearray(range(0, 255))

print(the_bytes)
print(the_byte_array)


"""Ch. 7.2.2"""

import struct

valid_png_header = b'\x89PNG\r\n\x1a\n'




"""Ch. 7.3"""

# 1.
mystery = '\U0001f4a9'
print(mystery)

import unicodedata
mystery_name = unicodedata.name(mystery)
print(mystery_name)

# 2.
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

# 3.
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
print(pop_string == mystery)

# 4.
print('My kitty cat likes %s, My kitty cat likes %s, My kitty cat fell on his %s And now thinks he\'s a %s'
      % ('roast beef', 'ham', 'head', 'clam'))

# 5.

letter = """Dear {salutation} {name},
            Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. 
            Please note that it should never be used in a {room}, especially near any {animals}.
            Send us your receipt and {amount} for shipping and handling. 
            We will send you another {product} that, in our tests, 
            is {percent}% less likely to have {verbed}.
            Thank you for your support.
                Sincerely,
                {spokesman}
                {job_title}
"""

# 6.
response = {'salutation': 'Mr.',
            'name': 'Kevin',
            'product': 'shampoo',
            'verbed': 'ranned out',
            'room': '1003',
            'animals': 'new room',
            'amount': '10',
            'percent': '1',
            'spokesman': 'Lisa',
            'job_title': 'manager'}

print(letter.format(**response))

# 7.
mammoth = """
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
"""

# 8.
import re
print(re.findall(r'\bc\w*', mammoth))

# 9.
print(re.findall(r'\bc\w{3}\b', mammoth))

# 10.
print(re.findall(r'\b\w*r\b', mammoth))
