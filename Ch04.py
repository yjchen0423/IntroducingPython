"""Ch 4.4.2"""

'continue'

while True:
    value = input('Please enter an integer, or "q" to quit: ')
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        print(f'The number {number} is a even number.')
        continue
    print(f'The number\'s square is {number * number}')

"""Ch 4.4.3"""

'while - else'

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += position + 1
else:  # if break is not executed
    print('No even number is found.')

"""Ch 4.5.1"""

'for else'


def prime_number(num):
    prime_numbers = []

    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)

    print(f'The prime numbers from 0 to {num} are: ')

    for k in prime_numbers:
        print(f'{k}')


prime_number(150)

"""Ch 4.5.4"""

'zip()'

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(f'{day}: drink {drink}, eat {fruit}, and enjoy {dessert}')


"""Ch 4.6"""
'comprehension 推導式'
'[expression for item in iterable]'

number_list = [number - 1 for number in range(1, 6)]
print(number_list)


'[expression for item in iterable if condition]'

a_list = [number for number in range(1, 10) if number % 2 == 0]
print(a_list)

rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

for row, col in cells:
    print(row, col)


'{key_expression: value_expression for expression in iterable}'

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)


"""Ch 4.7"""

'def() and return'
def echo(anything):
    return anything + ' ' + anything


def echo2(anything):
    print(f"{anything} {anything}")


echo('test1')
echo2('test2')

print(echo('test1'))


def commentary(color):
    if color == 'red':
        return 'it is a tomato.'
    elif color == 'green':
        return 'it is a green pepper.'
    elif color == 'bee purple':
        return 'i do not know this.'
    else:
        return 'enter color that I know!'


comment = commentary('red')
print(comment)


"""Ch 4.7.4"""

'*args'

def print_args(*args):
    print(f'there are several items here: {args}')


print_args(1, 2)
print_args(1, 2, 3, 'a')


"""Ch 4.7.5"""
'**kwargs'

def print_kwargs(**kwargs):
    print('keyword arguments: ', kwargs)


print_kwargs(wine='wine1', entree='entree1')
print_kwargs(wine='wine2', entree='entree2', dessert='dessert2')


"""Ch 4.7.7"""

'functions'

def answer():
    print(42)


answer()


def run_something(func):
    func()


run_something(answer)


def sum_args(*args):
    return sum(args)


def run_something2(func, *args):
    return func(*args)


print(run_something2(sum_args, 1, 2, 3, 4, 5))



"""Ch 4.7.8"""

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)



print(outer(4, 7))


"""Ch 4.7.10"""

'lambda(): lambda arguments: expression'


def edit_story(words, func):
    for word in words:
        print(func(word))


word_for_test = ['abcdef', 'bcdefg', 'cdefgh']



def enliven(word):
    return word.capitalize() + "!"


print(edit_story(word_for_test, enliven))
print(edit_story(word_for_test, lambda word: word.capitalize() + '!'))


"""Ch 4. 9"""

'Decorators: modify an existing function without changing its source code'


'example from https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-3-%E7%A5%9E%E5%A5%87%E5%8F%88%E7%BE%8E%E5%A5%BD%E7%9A%84-decorator-%E5%97%B7%E5%97%9A-6559edc87bc0'

# print_func_name is a decorator that
# adds one more line to indicate which function is used now

def print_func_name(func):
    def wrap():
        print("Now use function '{}'".format(func.__name__))
        func()
    return wrap



@print_func_name
def dog_bark():
    print("Bark !!!")


@print_func_name
def cat_miaow():
    print("Miaow ~~~")

dog_bark()  # since there is a '@'
cat_miaow()

'order of decortors'

def print_func_name2(func):
    def wrap2():
        print("Now use the function '{}'".format(func.__name__))
        func()
    return wrap2

def print_time(func2):
    import time
    def wrap3():
        print(f"Inner function is {func2.__name__}")
        print(f"Time is now '{int(time.time())}'.")
        func2()
    return wrap3


@print_func_name2
@print_time
def dog_bark2():
    print("Bark !!!")



dog_bark2()
# dog_bark2 is first entered as func2 in print_time
# then wrap3 in print_time is entered as func in print_func_name2
# displayed order:
# 1. print_func_name2, print out "Now use the function func(wrap3)"
# 2. execute func(), which is wrap3, print out Inner function is func2 (dog_bark2),
# 3. then print "Time is now..."
# 4. last in print_time, execute func2(), which is dog_bark2,
# 5. and print "Bark !!!"


'Example from book'


def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_function

def square_it(func):
    def new_func_suqare_it(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_func_suqare_it

def add_ints(a, b):
    return a + b

document_it(add_ints)(3, 5)
# document_it(func)(func's args)

@document_it
@square_it
def add_ints2(a, b):
    return a + b

add_ints2(4, 7)


"""Ch 4.10"""

'local & global'

animal = 'fruitbat'
def print_global():
    print("inside print_global: ", animal)

print("at the top level: ", animal)

print_global()


def change_and_print_global():
    print('inside change_and_print_global: ', animal)
    # animal = 'wombat'  # there will be an error
    print('after change:', animal)


def change_local():
    animal = 'wombat'
    print('inside change_local: ', animal, id(animal))

change_local()


ani2 = 'fruitbat2'
def cahnge_and_print_global2():
    global ani2
    ani2 = 'wombat'
    print('inside change_and_print_global: ', ani2)


print(ani2)
cahnge_and_print_global2()
print(ani2)


'_ and __'

def amazing():
    """This is the amazing function"""
    print(f'name: {amazing.__name__}')
    print(f'help docs: {amazing.__doc__}')


amazing()



"""Ch 4. 11"""

'try & except'

short_list = [1, 2, 3]
position = 5

try:
    short_list[position]
except:
    print(f'need a position between 0 and {len(short_list) - 1}, what we had is {position}')


'except exceptiontype as name'

while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        # Exception is all parent class of all errors
        print('Something is broken: ', other)


"""Ch 4.12"""

'costumed exceptions'
# class UppercaseException(Exception):
#     pass
#
# words = ['eenie', 'meenie', 'miny', 'MO']
#
#
# for word in words:
#     if word.isupper():
#         raise UppercaseException(word)




"""Ch 4.13 Exercise"""

# 1.
guess_me = 7

if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

# 2.
start = 1
while True:
    if start < guess_me:
        print(f'start is {start} and guess_me is {guess_me}')
        print('start is too low')
    elif start == guess_me:
        print(f'start is {start} and guess_me is {guess_me}')
        print('found it!')
        break
    else:
        print(f'oops')
        break
    start += 1

# 3.
j = []

for i in range(3, -1, -1):
    j.append(i)

print(j)

# 4.
even_num = [i for i in range(0, 10) if i % 2 == 0]

print(even_num)

# 5.
square_dict = {num:num*num for num in range(10)}

print(square_dict)

# 6.

