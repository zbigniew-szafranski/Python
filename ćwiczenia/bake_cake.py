class Cake:
    def __init__(self):
        self.baked = False
        self.ingredients = ["flower", "sugar", "eggs" ]

    def bake(self):
        print("Baking cake")
        self.baked = True

    def ready(self):
        return "Ready!" if self.baked else "Not ready yet!"

class ChocolatteCake(Cake):
    def __init__(self):
        super().__init__()
        self.ingredients.append("chocolatte")

    def bake(self):
        print("Melt chocolatte...")
        super().bake()
        print("Add chocolatte")

cake = Cake()
chocolatte_cake = ChocolatteCake()

print("Ingredients for cake: ", cake.ingredients)
print("Ingredients for chocolatte cake: ", chocolatte_cake.ingredients)

print("\nBaking cake:")
cake.bake()

print("\nBaking chocolatte cake:")
chocolatte_cake.bake()
print("Status:", chocolatte_cake.ready())

print("\nAre chocolatte cake?", isinstance(chocolatte_cake, Cake))
print("\nAre cake chocolatte?", isinstance(cake, ChocolatteCake))