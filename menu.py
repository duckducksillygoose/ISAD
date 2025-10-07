
#add some fileio stuff
import csv
from classfile import *

data = []

service_file = open("services.csv", "r")
reader = csv.reader(service_file)
rows = [row for row in reader if row]

i=0

while i<len(rows):
    if len(rows[i]) == 0:
        i+=1
        continue

    name= rows[i][0].strip()
    units = rows[i][1].strip()

    tiers =[float(x) for x in rows[i+1]]

    cost = [float(x) for x in rows[i+2]]


    i+=3

    data.append(Service(name, units, tiers, cost))

print(data)