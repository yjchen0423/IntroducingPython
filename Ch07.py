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

