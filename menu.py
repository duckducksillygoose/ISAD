
#add some fileio stuff
import csv

data = []

service_file = open("services.csv", "r")
reader = csv.reader(service_file)

rows = list(reader)

i=0

while i<len(rows):
    if len(rows[i]) == 0:
        i+=1
        continue

    name= rows[i][0].strip()
    units = rows[i][1].strip()

    tiers =[float(x) for x in rows[i+1]]

    cost = [float(x) for x in rows[i+2]]

    data.append(["name:", name, "units:", units, "tiers:", tiers, "cost: ", cost])

print()