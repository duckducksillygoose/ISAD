
class SubscriptionManager():
    def __init__ (self):
        self.subscriptions = []
    def overall_cost(self):
        return sum(s.cost for s in self.subscriptions)
    
    def add_subscription(self, type):
        self.subscriptions.append(type)
        print("Subscription added successfully :)")


class Service():
    def __init__ (self, name, units, tiers, cost):
        self.name = name
        self.units = units
        self.tiers = tiers
        self.cost =cost


    def get_price(self):
        amount = input("How much of this service would you like?")
        for i in range(len(self.tiers)-1):
            if self.tiers[i] < float(amount) <self.tiers[i+1]:
                cost=self.cost[i]
                print("The cost per unit for this amount is", self.cost[i])
                print("The total cost is", cost * float(amount))






        


        
    