#take airports.csv and sort it by airport name and export it as airports-sorted.txt and only have the airport name
import csv
import operator
with open('airports.csv', 'r') as f:
    reader = csv.reader(f)
    airports = list(reader)
airports.sort(key=operator.itemgetter(3))
with open('airports-sorted.txt', 'w') as f:
    for i in airports:
        f.write(i[3] + "\n")
