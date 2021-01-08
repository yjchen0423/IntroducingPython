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
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside setter')
        self.hidden_name = input_name


fowl2 = Duck2('Howard2')
print(fowl2.name)

