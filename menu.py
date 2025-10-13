

import csv
from classfile import *

manager = SubscriptionManager()
services=[]

def file_read():
    service_file = open("services.csv", "r")
    reader = csv.reader(service_file)
    rows = [row for row in reader if row]

    i=0


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
        service = Service(name, units, tiers, cost)
        services.append(service)


        i += 3  



#manager is for the subscriptions that the user has, while services is a list of services

#services is an object list
def load_menu():

    print("-------------WELCOME TO THE MENU-----------------")

    print("To add a subscription, press 1")
    print("To get rid of a subscription, press 2")
    print("Press s for the total breakdown of all subscriptions")
    print("Press Q to quit")



    answer = input("Please select your options")
    while answer !="Q":
        if answer == "1":
            sub_type = input("What subscription would you like?")
            print("You have selected", sub_type)
            
            found = False
            for s in services:
                if s.name.upper() == sub_type.upper() and s not in manager.subscriptions:
                    manager.add_subscription(s)
                    found = True
                    s.get_price()

                elif s in manager.subscriptions:
                    print("You already have this subscription")
                    found = True

            if not found:
                    print("We do not offer this subscription")


            print(manager.subscriptions)
        elif answer == "2":
            found = False
            to_delete = input("Which subscription would you like to delete? ")
            for entry in manager.subscriptions:
                if entry.name.upper() == to_delete.upper(): #if you already have it
                    manager.delete_subscription(entry)
                    found = True

                elif entry in services: #in services but do not have
                    print("We do offer this subscription, but you do not have it currently")
                    found = True
            
            if not found:
                print("Not a valid subscription")


                
        



        elif answer.upper() == "S":
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


        else:
            print("This is not a valid entry")


        answer = input("What would you like to do?")

    print("You are now exiting the menu")



if __name__ == "__main__":
    file_read()
    load_menu()