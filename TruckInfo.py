
class TruckInfo:  # Declaring truck class and keys to be used
    def __init__(self, location, mph, miles_driven, depart_time, packages):
        self.location = location
        self.mph = mph
        self.miles_driven = miles_driven
        self.time = depart_time
        self.depart_time = depart_time
        self.packages = packages

    def __str__(self):  #Override # Citation 2
        return "%s, %s, %s, %s, %s, %s" % (self.location, self.mph, self.miles_driven, self.time,
                                           self.depart_time, self.packages)

