import coffeeshop

myCoffee = coffeeshop.ConcreteCoffee()
print('Ingredients: '+myCoffee.get_ingredients()+'; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))
myCoffee = coffeeshop.Milk(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+'; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))
myCoffee = coffeeshop.Sugar(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+'; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

#coffeee with sugar
myCoffee_sugar = coffeeshop.ConcreteCoffee()
myCoffee_sugar = coffeeshop.Sugar(myCoffee_sugar)
print('Ingredients: '+myCoffee_sugar.get_ingredients())
