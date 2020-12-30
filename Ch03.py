"""
Ch 3.2.8
"""

'extend()'

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)


"""
Ch 3.2.9
"""
'insert()'

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(3, 'Gummo')
print(marxes)
marxes.insert(10, 'Karl')
print(marxes)

"""
Ch 3.8 Exercise
"""

# 1.
years_least = [1984, 1985, 1986, 1987, 1988]

# 2.
print(years_least[3])

# 3.
print(years_least[-1])

# 4.
things = ["mozzarella", "cinderella", "salmonella"]

# 5.
things[1] = things[1].capitalize()
print(things)

# 6.
things[0] = things[0].upper()
print(things)

# 7.
things.remove("salmonella")
print(things)

# 8.
surprise = ["Groucho", "Chico", "Harpo"]

# 9.
surprise[-1] = surprise[-1].lower()
print(surprise)

surprise[-1] = surprise[-1][::-1].title()
print(surprise)

# 10.
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}

# 11.
print(e2f['walrus'])

# 12.*
f2e = {}
for e, f in e2f.items():
    f2e[f] = e

print(f2e)

# 13.
print(f2e['chien'])

# 14.
print(e2f.keys())

# 15.
life = {'animals': {'cats': 'Henri', 'octopi': 'emus', 'Grumpy': 'Lucy'},
        'plants': {}, 'others': {}}
print(life)

# 16.
print(life['animals'])

# 17.
print(life['animals']['cats'])
