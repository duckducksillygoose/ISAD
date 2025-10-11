
#add some fileio stuff
import csv
from classfile import *

manager = SubscriptionManager()


service_file = open("services.csv", "r")
reader = csv.reader(service_file)
rows = [row for row in reader if row]

i=0
services = []

user_expenditure = 0


while i<len(rows):
    if len(rows[i]) == 0:
        i+=1
        continue

    
    name = rows[i][0].strip()
    units = rows[i][1].strip()
    tiers = [float(x) for x in rows[i+1]]
    cost = [float(x) for x in rows[i+2]]

    services=[]
    # create Service object and add it to the list
    service = Service(name, units, tiers, cost)
    services.append(service)


    i += 3  








print("-------------WELCOME TO THE MENU-----------------")

print("To add a subscription, press 1")
print("To get rid of a subscription, press 2")
print("Press s for the total breakdown of all subscriptions")
print("Press Q to quit")

subscriptions =[]

answer = input("Please select your options")
while answer !="Q":
    if answer == "1":
        sub_type = input("What subscription would you like?")
        print("You have selected", sub_type)

        if sub_type == "AI":
            services[0].get_price()
            manager.add_subscription(sub_type)
            
    

        elif sub_type == "Computing":
            services[1].get_price()
            manager.add_subscription(sub_type)

        elif sub_type == "Database":
            services[2].get_price()
            manager.add_subscription(sub_type)

        elif sub_type == "Integration":
            services[3].get_price()
            manager.add_subscription(sub_type)

        elif sub_type == "Networking":
            services[4].get_price()
            manager.add_subscription(sub_type)

        elif sub_type == "Storage":
            services[5].get_price()
            manager.add_subscription(sub_type)

    elif answer == "2":
        to_delete = input("Which subscription would you like to delete? ")
        if to_delete in manager.subscriptions:
            manager.delete_subscription(to_delete)
        else:
            print("Subscription not found.")


            
    



    elif answer.upper() == "S":
        pass


    else:
        print("This is not a valid entry")


    answer = input("What would you like to do?")

print("You are now exiting the menu")

