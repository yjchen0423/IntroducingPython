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

