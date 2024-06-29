# C950 -- Ameeruddin Shaik --- ID#011074833

import datetime
import csv
from PackageData import Package
from DistanceAndParse import find_distance, address_parse
from Hash import ChainingHashTable
from TruckInfo import TruckInfo

# Citations shown here are numbered (1,2,3...) and correspond to the Task-2 word document superscript numbers in the
# sources section

with open("addressesCSV.csv") as AddressCSV:
    AddressCSV = csv.reader(AddressCSV)
    AddressCSV = list(AddressCSV)
with open("distancesCSV.csv") as DistanceCSV:
    DistanceCSV = csv.reader(DistanceCSV)
    DistanceCSV = list(DistanceCSV)

                            # Citation 2,6
def loadPackageData(file):  # Loading the package data, at the bottom it is being added to the hash
    with open(file) as packs:
        packageData = csv.reader(packs, delimiter=',')  # Saved as CSV so the file type uses commas to separate
        next(packageData)
        for package in packageData:
            packID = int(package[0])
            packStreet = package[1]
            packCity = package[2]
            packState = package[3]
            packZip = package[4]
            packDeadline = package[5]
            packWeight = package[6]
            packNotes = package[7]
            packStatus = "Arrived at Hub"
            packDeparture_time = ''
            packDelivery_time = ''

            # Inserting Package info into the hash
            pack = Package(packID, packStreet, packCity, packState, packZip, packDeadline, packWeight, packNotes,
                           packStatus, packDeparture_time, packDelivery_time)
            packHash.insert(packID, pack)


# Creating instance of hash table class
packHash = ChainingHashTable()
loadPackageData('packagesCSV.csv')

# Origin of trucks and max speed declared
hub = "4001 South 700 East"  # Salt Lake City, UT 84107
speed = 18
# Loading all three trucks this way (suggested by professor)
t1 = TruckInfo(hub, speed, 0.0, datetime.timedelta(hours=8), [1, 13, 14, 15, 16, 19, 20, 25, 27, 29, 30, 31, 34, 37, 40])#15
t2 = TruckInfo(hub, speed, 0.0, datetime.timedelta(hours=11), [2, 3, 4, 5, 9, 18, 26, 35, 36, 38])#10
t3 = TruckInfo(hub, speed, 0.0, datetime.timedelta(hours=9, minutes=5), [6, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24,
                                                                         28, 32, 33, 39])#15


def Delivery(trucks):  # Citation 1, 2, 3, 4, 6, 7
    in_progress = []  # Empty list that will contain the packages not yet delivered
    for packageID in trucks.packages:  # Loops and adds package to the empty list
        package = packHash.search(packageID)
        in_progress.append(package)
    trucks.packages.clear()

    while len(in_progress) > 0:  # While in_progress is != empty
        next_location = 99999
        next_package = None          # Address parse being used to access the address
        for package in in_progress:  # Using the find_distance function, get distance between truck and package location
            if find_distance(address_parse(trucks.location), address_parse(package.address)) <= next_location:
                next_location = find_distance(address_parse(trucks.location), address_parse(package.address))
                next_package = package

        trucks.packages.append(next_package.ID)  # Adding Package, then removing it from list
        in_progress.remove(next_package)
        trucks.miles_driven += next_location  # Keeping track of the mileage
        trucks.location = next_package.address
        trucks.time += datetime.timedelta(hours=next_location / speed)
        next_package.delivery_time = trucks.time  # Updating times
        next_package.departure_time = trucks.depart_time


Delivery(t1)  # Calling Delivery, will put in motion the algorithm above.
Delivery(t3)  # Calling Delivery
t2.depart_time = min(t1.time, t3.time)  # Method of delaying truck 2 so it leaves later (because only 2 drivers)
Delivery(t2)  # Calling Delivery        # This has to be done because there are 2 drivers and 3 truck
                                        # Not possible for 1 driver to drive 2 trucks at the same time

def truck_miles():  # Function to get the combined miles, called in the menu interface by user
    combined_miles = t1.miles_driven + t2.miles_driven + t3.miles_driven  # Adding miles from all three trucks
    print("\nThe total combined miles of all three trucks -- ", combined_miles, "miles\n")  # Printing

# NOT USING, too much to print, takes up the whole console
# print("\nWGUPS --  The Official Postal Service of Western Governors University --")
# print("\nWe pride ourselves in being the most efficient Postal Service in UTAH!")
# print("---------")
# print("Don't believe us? Check below for how little miles we drove to deliver a whopping 40 packages!!!")
# print("---------")
# print("The total combined miles of all three trucks -- ", combined_miles, "miles")


# Looping to get data from hash, prints out basically everything in the file. From Dr. Cemal webinars
def getPackageData():  # Citation 2,6
   for p in range(len(packHash.table)):
       print(" Key: {} Package: {}".format(p, packHash.search(p+1)))
# getPackageData() check to see if working


def single_package_status():  # Gets single package
    id_entered = input("Enter the ID of the package you want to check --> :")  # Gets user input
    int(id_entered)
    package = packHash.search(int(id_entered))  # Searching hash
    package.override_status(time)
    print(str(package))  # Printing package

                                # Citation 6
def all_package_with_miles():  # Gets all packages
    package_rows = range(1, 41)  #40 cuts last package
    for packageID in package_rows:
        package = packHash.search(packageID)
        package.override_status(time)
        print(str(package))  # Printing package
    # Pseudo -- If packageID == 9 or ...  AND package.delivery_time > 10:30, print("Missed Delivery window")

if __name__ == '__main__':
    print("\n\nWelcome to WGUPS!\n\n")

    # Using a while loop so that it HAS to run at least once to show up on the console for the user
    # Is going to continue to show the menu until the user enters a valid option or exits, and after they select
    # Stays on the screen even after selection (unless '5' is selected) so the user can make more selections
    boolValue = True
    while boolValue:
        print("***********************************************")
        print("1. Get All Package Status and Total Mileage")
        print("2. Get a Single Package Status with a Time")
        print("3. Get Total Miles Driven to deliver all packages")
        print("4. Exit the Program")
        print("***********************************************")
        selected = input("Please select an option -- 1, 2, 3, or 4 -- : ")
        if selected == '1':
            time_entered = input(
                "Enter the time you want to check (24-hour clock) --> HOURS:MINUTES: ")
            (hours, minutes) = time_entered.split(":")
            int(hours)
            int(minutes)
            time = datetime.timedelta(hours=int(hours), minutes=int(minutes))
            all_package_with_miles()
            truck_miles()
        elif selected == '2':
            time_entered = input("Enter the time for one or more packages you want to check (24-hour clock) --> "
                                 "HOURS:MINUTES: ")
            (hours, minutes) = time_entered.split(":")
            int(hours)
            int(minutes)
            time = datetime.timedelta(hours=int(hours), minutes=int(minutes))
            single_package_status()
        elif selected == '3':
            truck_miles()
        elif selected == '4':
            boolValue = False  # Break from loop and exit
        else:
            print("Not a valid selection, please try again.")  # Error checking
