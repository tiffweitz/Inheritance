class PizzaPlaceMenu:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def printMenu(self):
        print (self.item + " $" + str(self.price))    
class Pizza(PizzaPlaceMenu):
    def __init__(self, item, price, size, topping):
        super().__init__(item, price)
        self.size = size
        self.topping = topping
    def bake(self):
        print( self.size + " size pizza with is in the oven.")
    def pizzaType(self):
        print(self.topping)
class Wings(PizzaPlaceMenu):
    def __init__(self, item, price, count, flavor):
        super().__init__(item, price)
        self.count = count
        self.flavor = flavor
    def getDippingSauce(self):
        self.dipSauce = print(input("Ranch or Bleu Cheese? "))
    def getWings(self):
        print("You have ordered " + str(self.count) + " wings. This costs $" + str(self.price))
class Soda(PizzaPlaceMenu):
    def __init__(self, item, price, size, sodaType):
        super().__init__(item, price)
        self.size = size
        self.sodaType = sodaType
    def makeDrink(self):
        print("Your " + self.size + " " + self.sodaType + " is being prepared.")
cheesePizza = Pizza("pizza", 15, "large", "cheese")
cheesePizza.bake()
cheesePizza.pizzaType()
myWings = Wings("wings", 10, 12, "buffalo")
myWings.getDippingSauce()
myWings.getWings()
myDrink = Soda("drink", 2, "medium", "coke")
myDrink.makeDrink()
myDrink.printMenu()