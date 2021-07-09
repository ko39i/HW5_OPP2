1.


class Laptop:
    def __init__(self):
        battery = Battery('This is charge for battery')
        self.battery = [battery]


class Battery:
    def __init__(self, charge):
        self.charge = charge


laptop = Laptop()

2.


class Guitar:
    def __init__(self, guitarstring):
        self.guitarstring = guitarstring


class GuitarString:
    def __init__(self):
        pass


guitarstring = GuitarString()
guitar = Guitar(guitarstring)

3.
import datetime

class Calc:
    @staticmethod
    def add_nums(x, y, z):
        return print(x + y + z)

calc = Calc()
calc.add_nums(3, 4, 5)

4.
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pasta ({self.ingredients})'

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


print(Pasta.carbonara())
print(Pasta.bolognaise())

5
class Concert:
    def __init__(self, max_visitors_num):
        self.max_visitors_num = max_visitors_num

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        self._visitors_count = value if value < self.max_visitors_num else self.max_visitors_num



concert = Concert(50)
concert.visitors_count = 1000
print(concert.visitors_count)