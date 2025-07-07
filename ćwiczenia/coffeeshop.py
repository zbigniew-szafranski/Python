import six
from abc import ABCMeta

@six.add_metaclass(ABCMeta)
class AbstractCoffee(object):

    def get_cost(self):
        return 0.0

    def get_ingredients(self):
        pass

    def get_tax(self):
        return round(0.1*self.get_cost(), 2)

class ConcreteCoffee(AbstractCoffee):

    def get_cost(self):
        return 1.00

    def get_ingredients(self):
        return 'coffee'

@six.add_metaclass(ABCMeta)
class AbstractCoffeeDecorator(AbstractCoffee):

    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()

class Sugar(AbstractCoffeeDecorator):
    def __init__(self, decorated_coffee):
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', sugar'

class Milk(AbstractCoffeeDecorator):
    def __init__(self, decorated_coffee):
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.25

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', milk'

class Vanilla(AbstractCoffeeDecorator):
    def __init__(self, decorated_coffee):
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.75

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', vanilla'

