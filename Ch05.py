"""Ch 5.5.1"""

'setdefault()'

periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
carbon

print(periodic_table)

helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)

from collections import defaultdict
periodic_table = defaultdict(int)

periodic_table['Hydrogen'] = 1
print(periodic_table['Lead'])

print(periodic_table)


"""Ch 5.5.5"""

'itertools'

import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

'accumulate()'

for item in itertools.accumulate([1, 2, 3, 4, 5]):
    print(item)

'use function as second argument in accumulate'
def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4, 5], multiply):
    print(item)


"""Ch 5.5.6"""

'pprint()'

from pprint import pprint
quotes = [(1, 'aaaaaaaa'),
          (2, 'bbbbbbbb'),
          (3, 'cccccccc'),
          (4, 'dddddddd')]

print(quotes)
pprint(quotes)
