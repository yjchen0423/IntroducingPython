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