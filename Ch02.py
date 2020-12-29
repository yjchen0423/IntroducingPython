"""2.3.3"""
palindrome = 'A man, \nA plan, \nA canal:\nPanama.'
print(palindrome)

print('\tabc')
print('a\tbc')
print('')

print('release the karken! ' + 'At once!')

'2.3.4'
a = 'Duck.'
b = a
c = 'Grey Duck!'

print(a + b + c)
print(a, b, c)


'2.3.5'
start = 'Na. ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'goodbye.'

print(start + start + middle + end)


'2.3.6'
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])

print(letters[-1])
print(letters[-2])

print(letters[25])
print(letters[5])
# print(letters[100])

name = 'Henny'
print(name.replace('H', 'P'))
print('P' + name[1:])


'2.3.7'
"""
[start:end:step]
"""
print(letters[:])
print(letters[20:])
print(letters[10:])
print(letters[12:15])
print(letters[-3:])

print(letters[18:-3])
print(letters[::7])
print(letters[4:20:3])

print(letters[19::4])
print(letters[:21:5])

print(letters[-1::-1])
print(letters[::-1])

print(letters[-51:-50])
print(letters[:70])
print(letters[70:71])


"""
Ch. 2.3.8
"""
'len()'

print(len(letters))


"""
Ch. 2.3.9
"""

'split()'

todos = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split(','))


"""
Ch. 2.3.10
"""

'join()'

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ','.join(crypto_list)
print(crypto_string)


"""
Ch 2.3.11
"""

'Practice'
poem = '''
All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.
'''

print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('That\'s all, folks!'))
word = 'the'
print(poem.find(word))
print(poem.rfind(word))
print(poem.count(word))
print(poem.isalnum())


"""
Ch 2.3.12
"""

setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())

'string in a fix length'
print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))


"""
Ch 2.3.13
"""

'replace()'

print(setup.replace('duck', 'marmoset'))
print(setup.replace('a ', 'a famous', 100))



"""
Ch 2.4
"""

'Exercies'

print(60*60)
seconds_per_hour = 60 * 60
print(seconds_per_hour)

seconds_per_day = 60 * 60 * 24
print(seconds_per_day)

print(seconds_per_day/seconds_per_hour)
print(seconds_per_day//seconds_per_hour)