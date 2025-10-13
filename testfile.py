from classfile import *
from menu import *

manager= SubscriptionManager()

netflix = Service("Netflix", "per month", [1, 4, 7], [28, 18, 10])
spotify = Service("Spotify", "per month", [10, 40, 100], [12.0, 7.0])
youtube = Service("Youtube", "per month", [1, 2, 3], [19, 16, 13])

services = [netflix, spotify, youtube]