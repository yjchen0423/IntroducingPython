# 1.

import zoo
zoo.hours()

# 2.
import zoo as menagerie
menagerie.hours()

# 3.
from zoo import hours
hours()

# 4.
from zoo import hours as info
info()

# 5.
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

# 6.
from collections import OrderedDict
fancy = OrderedDict(plain)
print(fancy)

# 7. *
from collections import defaultdict
dict_to_list = defaultdict(list)
dict_to_list['a'].append('something for a')
print(dict_to_list['a'])

