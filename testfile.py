from classfile import *
from menu import *

manager= SubscriptionManager()

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
