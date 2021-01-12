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
"""