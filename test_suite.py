from classfile import *
from menu import *
import time

manager = SubscriptionManager()

###we are testing add subscription, delete subscription and get_price

# Create your test services
netflix = Service("Netflix", "per month", [0, 4, 7], [28, 18, 10])
spotify = Service("Spotify", "per month", [0, 40, 100], [12.0, 7.0, 5.0])
youtube = Service("Youtube", "per month", [0, 20, 300], [19, 16, 13])

services = [netflix, spotify, youtube]

print("=== COMPREHENSIVE TEST SUITE ===\n")

print("----- BLACK-BOX TESTS --------")

print("1. Testing Initial State")
assert manager.overall_cost() == 0, "Initial cost should be zero since no subscriptions"
print("PASS: Initial manager has zero cost")

print("2. Testing Adding Subscriptions")
print("Adding Netflix")
manager.add_subscription(netflix)
print("Manager subscriptions:", [s.name for s in manager.subscriptions])
assert len(manager.subscriptions) == 1, "Should have 1 subscription"
print("PASS: Netflix added successfully")

print("Trying to add Netflix again (duplicate)")
manager.add_subscription(netflix)
assert manager.subscriptions.count(netflix) == 1, "Netflix should only be once in the list"
print("PASS: Duplicate Netflix prevented")


print("Adding Spotify")
manager.add_subscription(spotify)
print("Current subscriptions:", [s.name for s in manager.subscriptions])
assert len(manager.subscriptions) == 2, "Should have 2 subscriptions"
print("PASS: Spotify added successfully")




