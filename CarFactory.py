class CarFactory:
    #Defines CarFactory class
    def __init__(self, make, model, year, price):
        self.make = make
        #Creates an instance variable of make.
        self.model = model
        #Creates an instance variable of model.
        self.year = year
        #Creates an instance variable of year.
        self.price = price
        #Creates an instance variable of price.
        self.tax = self.price * 0.20
        #Creates an instance variable of tax.
        self.totalPrice = self.tax + self.price
        #Creates an instance variable of totalPrice.
        #This is the constructor for the CarFactory class.
        #I passed in the arguments make, model, year, and price.


    def infoDisplay(self):
    #Defines the infoDisplay method, which takes in the class' instance variables as arguments.
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")
        print(f"Tax: {self.tax}")
        print(f"Total: {self.totalPrice}")
Lamborghini = CarFactory("Lamborghini", "Aventador", 2020, 100000)
#Creates an instance(an object) of the CarFactory class.
Lamborghini.infoDisplay()
#Calls on the infoDisplay method.