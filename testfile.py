from classfile import *
from menu import *
import time

manager= SubscriptionManager()
assert manager.overall_cost() == 0, "Initial cost should be zero since no subscriptions"

###we are testing add subscription, delete subscription and get_price



netflix = Service("Netflix", "per month", [1, 4, 7], [28, 18, 10])
spotify = Service("Spotify", "per month", [10, 40, 100], [12.0, 7.0])
youtube = Service("Youtube", "per month", [1, 2, 3], [19, 16, 13])

services = [netflix, spotify, youtube]


print("-----ADDING SUBSCRIPTIONS-------")


print("Adding netflix")
a1 = manager.add_subscription(netflix)
print("Manager subscriptions:", [s.name for s in manager.subscriptions])
netflix.get_price()


##duplicate
print("Trying to add netflix again")
a2 = manager.add_subscription(netflix)
assert manager.subscriptions.count(netflix) == 1, "Netflix should only be once in the list"

print("Current subscriptions:", [s.name for s in manager.subscriptions])



print()
print()

print("Adding spotify")
a3 = manager.add_subscription(spotify)
print("Current subscriptions:", [s.name for s in manager.subscriptions])
spotify.get_price()

print()
print()




print("----DELETING SUBSCRIPTIONS--------")
d1 = manager.delete_subscription(netflix)
print("Deleted Netflix")
print("Current subscriptions", [s.name for s in manager.subscriptions])
assert netflix not in manager.subscriptions, "Subscription should be removed"


print("Trying to delete youtube")
d2 = manager.delete_subscription(youtube) #not in list


print("TOTAL SUBSCRIPTION COSTS")

print("Your subscriptions are as follows:")
total = 0
for entry in manager.subscriptions:
    print("Subscription: ", entry.name)
    print("Units: ", entry.units)
    print("Overall cost", entry.overall)


    print()
    print()

    total +=entry.overall
    print("Your total subscription costs are:" ,total)

assert manager.overall_cost !=0, "Should have services"


time.sleep(1)

print("Now we will be testing the boundary values of each")
print("Add 4 hours of netflix, price should be 18 ")
t1= manager.add_subscription(netflix)
netflix.get_price()
manager.delete_subscription(netflix)

print("Now we are adding 3.99 hours of netflix, price should be 28")

manager.add_subscription(netflix)
netflix.get_price()
manager.delete_subscription(netflix)

print("Add 4.01 hours of netflix, unit price should be 18")
t1= manager.add_subscription(netflix)
netflix.get_price()
manager.delete_subscription(netflix)
