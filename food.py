class foodNDD:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount #mass of the food in pounds
        self.price = 0 #standard price of the food per pound in dollars
        self.total = 0 #calculated total price
        
        def pricelistNDD(self): #setting standard price of the food
            if self.name=="Dry Cured Iberian Ham":
                self.price=177.8
            elif self.name=="Wagyu Steaks":
                self.price=450
            elif self.name=="Matsutake Mushrooms":
                self.price=272
            elif self.name=="Kopi Luwak Coffee":
                self.price=306.5
            elif self.name=="Moose Cheese":
                self.price=487.2
            elif self.name=="White Truffles":
                self.price=3600
            elif self.name=="Blue Fin Tuna":
                self.price=3603
            elif self.name=="Le Bonnotte Potatoes":
                self.price=270.81
            else:
                self.price=0
        
        def totalNDD(self):
            self.pricelistNDD
            self.total=self.price*self.amount #total cost calculation
            return self.total
        
        def __str__(self):
            self.__pricelistNDD()
            return f"Name: {self.name}\n Amount(pounds): {self.amount}\n Price: {self.price}\n Total: {self.total}"
