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

#FULL LIST OF TESTS






#error cases

#do netflix.calculatecost(negative)
#except ValueError(print(Pass))

#test the zero



#test the removal of a subscription you don't have



#TESTING COST CALCULATIONS (more whitebox)

#netflix calculate cost as well as spotify
result_cc = netflix.get_price(1)
expected_cc = 1*28 #28
assert result_cc == expected_cc, "Test failed, calculated incorrect result"
print("PASS: Tier 1 works")

#tier 2 test
result_t2 = netflix.calculate_cost(4) #should be 18 x 4
expected_t2 = 4*18
assert result_t2 == expected_t2, "Test failed, did not return the correct amount"
print("Tier 2 works")


#tier 3 test
result_t3 = netflix.calculate_cost(7) #should be 70
expected_t3 = 70
assert result_t3 == expected_t3
print("Tier 3 works")


#inbetween testing

result_it = netflix.calculate_cost(2) #should be 2 x 28 or 56
expected_it = 2*28
assert result_it == expected_it
print("Tier 4 works")


#large value testing

result_large = netflix.calculate_cost(1000)
expected_large = 10000
assert result_large == expected_large
print("This program handles large values well")













