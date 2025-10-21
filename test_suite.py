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
