import csv
import pandas

file1 = 'C127HWData.csv'
file2 = 'dwarf_stars.csv'
d1 = []
d2 = []

with open (file1, 'r') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        d1.append(i)

with open (file2, 'r') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        d2.append(i)

header1 = d1[0]
header2 = d2[0]

data = d1[1:]
data2 = d2[1:]

header = header1 + header2

allData = []

for i in data:
    allData.append(i)

for i in data2:
    allData.append(i)

with open("totalstars.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(allData)