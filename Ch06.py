"""Ch. 6.2"""

'class'

class Person():
    def __init__(self, name):
        self.name = name



hunter = Person('Fudd')

print(f'The hunter\'s name is: {hunter.name}.')


"""Ch. 6.3"""


class Car():
    def exclaim(self):
        print('I am a car!')


class Yugo(Car):
    pass


give_me_a_car = Car()
give_me_a_yugo = Yugo()


give_me_a_car.exclaim()
give_me_a_yugo.exclaim()


"""Ch. 6.4"""

'override a method'


class Car():
    def exclaim(self):
        print('I am a car!')


class Yugo(Car):
    def exclaim(self):
        print('I am a Yugo!')


give_me_a_car = Car()
give_me_a_yugo = Yugo()


give_me_a_car.exclaim()
give_me_a_yugo.exclaim()



class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"


person = Person("Fudd")
doctor = MDPerson("Fudd")
lawyer = JDPerson("Fudd")

print(person.name)
print(doctor.name)
print(lawyer.name)


"""Ch. 6.5"""
'Add a new method'


class Car():
    def exclaim(self):
        print("I'm a car!")


class Yugo(Car):
    def exclaim(self):
        print("I am a yugo!")

    def need_a_push(self):
        print("Help me?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

# give_me_a_car.need_a_push()
give_me_a_yugo.need_a_push()



"""Ch. 6.6"""


'super() - after calling a child method from child class, ' \
'I also want to call it from parent'


class Person():
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        # use super() and do not need to rewrite __init__.name again
        self.email = email


bob = EmailPerson('Bob', 'bob@yahoo.com')
print(bob.name)
# no () after name because it is not a method
print(bob.email)



"""Ch. 6.8"""

'attribute access: ' \
'object attributes that cannot be accessed directly from outside'

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('Inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)
    # first argu in property is getter (to get the value of property)
    # second argu is setter (to set the value of property)

fowl = Duck('Howard')
print(fowl.name)
print(fowl.get_name())

fowl.set_name('Daffy')
print(fowl.name)
print(fowl.get_name())


'Use decorator to indicate getter and setter'

class Duck2():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    # as getter
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    # as setter
    def name(self, input_name):
        print('inside setter')
        self.hidden_name = input_name


fowl2 = Duck2('Howard2')
# apply Howard2 as input_name of argu in __init__
print(fowl2.name)
# get the name using getter, so it returns self.hidden_name
fowl2.name = 'Donald'
# setter: set Donald as input_name in setter name
print(fowl2.name)
# get the name using getter again



class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 7
print(c.diameter)

# since there is no setter for diameter (@diameter.setter),
# we cannot change diameter value from outside


"""Ch. 6.9"""

'begin with two underscores (__)'

class Duck3():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print("inside the getter")
        return self.__name
    @name.setter
    def name(self, input_name):
        self.__name = input_name


fowl3 = Duck3('Howard3')
print(fowl3.name)
fowl3.name = 'Donald2'
print(fowl3.name)


"""Ch. 6.10"""
'instance method - have self argument in methods within a class'
'class method - affects the class as a whole, use @classmethod decorator'

class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print('I am an A!')
    @classmethod
    def kids(cls):
        print(f'A has {cls.count} little objects.')

A1 = A()
A2 = A()
A3 = A()
A4 = A()
A.kids()


'staticmethod - do not need to create class object'

class CoyoteWeapon():
    @staticmethod
    def commerical():
        print('This CoyoteWeapon has been brought to you by Acme!')

# no need to create an object like C = CoyoteWeapon()
CoyoteWeapon.commerical()



"""Ch. 6.11"""

'polymorphism'

class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


hunter1 = Quote('Fudd', 'I am hunting rabbits')
print(f'{hunter1.who()} says {hunter1.says()}')

hunted1 = QuestionQuote('Bunny', 'What\'s up, doc')
print(f'{hunted1.who()} says {hunted1.says()}')

hunted2 = ExclamationQuote('Duck', 'It\'s rabbit')
print(f'{hunted2.who()} says {hunted2.says()}')


# -----------

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()



def who_says(obj):
    print(f"{obj.who()} says {obj.says()}")

# plug object (hunter1, hunted1, hunted2, brook that were created through class)
# brook is not child of Quote so it will not return the same conents as them
who_says(hunter1)
who_says(hunted1)
who_says(hunted2)
who_says(brook)


"""Ch. 6.12"""

'magic method'


'__eq__'
'__repr__'
class Word():
    def __init__(self, text):
        self.text = text
    # def equals(self, word2):
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("' + self.text + '")'



first = Word("ha")
second = Word("HA")
third = Word("eh")

# print(first.equals(second))
# print(first.equals(third))
print(first == second)
print(first == third)


print(first)
first


"""Ch. 6.13"""

'Aggregation and Composition'

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print(f"This duck has a {bill.description} bill and a {tail.length} tail.")


tail = Tail('long')
bill = Bill('wild orange')
duck = Duck(tail, bill)
duck.about()



"""Ch. 6.15"""

# 1.
class Thing():
    pass

print(Thing)
example = Thing()
print(example)

# 2.
class Thing2():
    letters = 'abc'

print(Thing2.letters)

# 3.
class Thing3():
    def __init__(self):
        self.letters = 'xyz'

thing3 = Thing3()
print(thing3.letters)

# 4.
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


element1 = Element('Hydrogen', 'H', 1)
print(element1.name)
print(element1.symbol)
print(element1.number)

# 5.
dict1 = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(dict1['name'], dict1['symbol'], dict1['number'])
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)

# 6.
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        return f"The element's name is {self.name}, symbol is {self.symbol}, and number is {self.number}."

hydrogen = Element(dict1['name'], dict1['symbol'], dict1['number'])
print(hydrogen.dump())

# 7.
print(hydrogen)
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return f"The element's name is {self.name}, symbol is {self.symbol}, and number is {self.number}."


hydrogen = Element(dict1['name'], dict1['symbol'], dict1['number'])
print(hydrogen)

# 8.
class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

hydrogen = Element(dict1['name'], dict1['symbol'], dict1['number'])
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)

# 9.
class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

bear1 = Bear()
print(bear1.eats())

rabbit1 = Rabbit()
print(rabbit1.eats())

octothorpe1 = Octothorpe()
print(octothorpe1.eats())

# 10.
class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self, laser, claw, smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone =smartphone
    def does(self):
        return f'robots can do {self.laser.does()}, {self.claw.does()}, and {self.smartphone.does()}'

laser1 = Laser()
claw1 = Claw()
smartphone1 = SmartPhone()
robot1 = Robot(laser1, claw1, smartphone1)
print(robot1.does())
