import csv

# Making all files accessible
with open("addressesCSV.csv") as AddressCSV:
    AddressCSV = csv.reader(AddressCSV)
    AddressCSV = list(AddressCSV)


# Parse addresses from the CSV file so they can be used
def address_parse(add):  # Citation 5
    for row in AddressCSV:
        if add in row[2]:  # May need to str(add)
            return int(row[0])  # This is the ID row


# Making all files accessible
with open("distancesCSV.csv") as DistanceCSV:
    DistanceCSV = csv.reader(DistanceCSV)
    DistanceCSV = list(DistanceCSV)


# def find_distance(x, y):  # Should get the distance between two vertices (addresses), this is called in
# The algorithm to get the distances between vertices
def find_distance(xad, yad):
    distance = DistanceCSV[xad][yad]
    if distance == '':
        distance = DistanceCSV[yad][xad]
    return float(distance)
