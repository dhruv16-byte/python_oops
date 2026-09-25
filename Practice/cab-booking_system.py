class Cab:
    def __init__(self, car_number, driver_name,cab_type, fare_per_km):
        self.car_number=car_number
        self.driver_name=driver_name
        self.cab_type=cab_type
        self.fare_per_km=fare_per_km
        self.available=1

class Cabbooking :
    def __init__(self):
        self.list_cab=[]
        self.bookings = []
        
    def addcab(self, obj_cab):
        self.list_cab.append(obj_cab)

    def display_cabs(self):
        for i in self.list_cab:
            if i.available==1:
                print(f"Car Number : {i.car_number}\nDriver name : {i.driver_name}\nCab type : {i.cab_type}\nFare per km : {i.fare_per_km}")

    def book_cab(self, obj_cab, dis):
        if obj_cab.available==1:
           obj_cab.available=0
           fare=dis*obj_cab.fare_per_km
           self.bookings.append((obj_cab,fare))
        else :
            print("The cab is not available")

    def display_details(self):
        for j,i in self.bookings:
            print(f"Car number : {j.car_number}\nDriver name : {j.driver_name}\nCab type : {j.cab_type}\nFare per km : {j.fare_per_km}\nFare : {i}")