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





"""Ch 4.13 Exercise"""
