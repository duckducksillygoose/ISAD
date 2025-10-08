
#add some fileio stuff
import csv
from classfile import *

data = []


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

    # create Service object and add it to the list
    service = Service(name, units, tiers, cost, 0)
    services.append(service)

    i += 3  


AI = services[0]
Computing = services[1]
Integration=services[2]
Networking = services[3]
Database = services[4]
Storage = services[5]





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
            AI.get_price()
            
    

        elif sub_type == "Computing":
            Computing.get_price()

        elif sub_type == "Database":
            Database.get_price()

        elif sub_type == "Integration":
            Integration.get_price()

        elif sub_type == "Networking":
            Networking.get_price()

        elif sub_type == "Storage":
            Storage.get_price()

    elif answer == "2":
        pass

    elif answer.upper() == "S":
        pass


    else:
        print("This is not a valid entry")

print("You are now exiting the menu")

