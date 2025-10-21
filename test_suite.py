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
print("zero initial cost")

print("2. Testing Adding Subscriptions")
print("Adding Netflix")
manager.add_subscription(netflix)
print("Manager subscriptions:", [s.name for s in manager.subscriptions])
assert len(manager.subscriptions) == 1, "Should have 1 subscription"
print("Netflix added successfully")

print("Trying to add Netflix again (duplicate)")
manager.add_subscription(netflix)
assert manager.subscriptions.count(netflix) == 1, "Netflix should only be once in the list"
print("Duplicate Netflix prevented")


print("Adding Spotify")
manager.add_subscription(spotify)
print("Current subscriptions:", [s.name for s in manager.subscriptions])
assert len(manager.subscriptions) == 2, "Should have 2 subscriptions"
print("Spotify added successfully")


#error cases

#do netflix.calculatecost(negative)
#except ValueError(print(Pass))

#test the zero



#test the removal of a subscription you don't have



#TESTING COST CALCULATIONS (more whitebox)

print("_____________WHITEBOX TESTING___________________")

#netflix calculate cost as well as spotify
result_cc = netflix.calculate_cost(1)
expected_cc = 1*28 #28
assert result_cc == expected_cc, "Test failed, calculated incorrect result"
print("Tier 1 works")

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

result_large = spotify.calculate_cost(1000)
expected_large = 1000*5
assert result_large == expected_large
print("This program handles large values well")




#ERROR CASES

print("\n4. Testing Error Cases")
# Test negative amount
try:
    netflix.calculate_cost(-1)
    assert False, "Should have raised ValueError for negative amount"
except ValueError:
    print("Negative amount correctly raises error")

# Test zero amount
result4 = netflix.calculate_cost(0)
assert result4 == 0, "Zero amount should cost zero"
print("Zero amount handled correctly, test passed")

print("Subscription removal testing")

print("Removing Netflix")
manager.delete_subscription(netflix)
assert netflix not in manager.subscriptions, "Netflix should be removed"
assert len(manager.subscriptions) == 1, "Should have 1 subscription left"


#add_subscription internal logic tests
test_manager = SubscriptionManager()
test_manager.add_subscription(spotify)

assert test_manager.subscriptions[0].name == "Spotify"
assert test_manager.subscriptions[0].units == "per month"
print("Internal list contains correct data")



test_manager.add_subscription(netflix)
stored_service = test_manager.subscriptions[0]
assert stored_service is netflix, "not the same object"  # should be same object
print("Same object reference stored internally")



print("ALL TESTS PASSED AND COMPLETED")













