import csv
from Hash import ChainingHashTable
import datetime


# Format according to possible output example from 'implementation steps' page.
# Functions adapted from Dr. Cemal Tepe's C950 Webinars
                # Citation 1,2
class Package:  # Making the class package, declaring the keys that will be used
    def __init__(self, ID, address, city, state, zip, deadline, weight, notes, status, departure_time, delivery_time):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.departure_time = ''
        self.delivery_time = ''

    def __str__(self):  # Override # Citation 2
        return "ID: %s, %s, %s, %s,%s, Delivery deadline: %s,%s Kg,%s, Departure Time: %s, Actual Delivery Time: %s" % (
            self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.status,
            self.departure_time, self.delivery_time)

    def override_status(self, difference):  # Alters package status. Deals with the package with wrong address
        if self.delivery_time == '':  # That WGUPS will be informed about at 10:20AM
            self.status = "Arrived At Hub"
        elif difference < self.departure_time:
            self.status = "Arrived At Hub"
        elif difference < self.delivery_time:
            self.status = "OTW"
        else:
            self.status = "Delivered"

        if self.ID == 9:  # This is the package with the wrong address that needs to be changed
            if difference > datetime.timedelta(hours=10, minutes=20):  # The time we are informed about new address
                self.address = "410 S State St"  # Proper address
                self.zip = "84111"
            else:
                self.address = "300 State St"  # Improper address
                self.zip = "84103"
