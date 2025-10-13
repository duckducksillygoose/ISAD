
class SubscriptionManager():
    def __init__ (self):
        self.subscriptions = []
    def overall_cost(self):
        return sum(s.overall for s in self.subscriptions)
    
    def add_subscription(self, type):
        if type not in self.subscriptions:
            self.subscriptions.append(type)
            print("Subscription added successfully :)")

        else:
            print("Service has already been susbcribed to")

    def delete_subscription(self, type):
        self.subscriptions.remove(type)
        print("subscription removed successfully :)")


class Service():
    def __init__ (self, name, units, tiers, cost):
        self.name = name
        self.units = units
        self.tiers = tiers
        self.cost =cost
        self.overall = 0


    def get_price(self):
        amount = float(input("How much of this service would you like?"))

        cost = None
        for i in range(len(self.tiers)):
 
            if i == len(self.tiers) - 1 or (self.tiers[i] <= amount < self.tiers[i + 1]):
                cost = self.cost[i]

        if cost is not None:
            total = cost * amount
            print("The cost per unit for this amount is", cost)
            print("The total cost is", total)
            self.overall = total
            print()
            print()
        else:
            print("Could not determine price for this amount.")
                






        


        
    