class Vehicle:
    def __init__(self,make,model,is_available):
        self.make= make
        self.model = model
        self.is_available = is_available
        
    def display_info(self):
        status = "Available" if self.is_available else "Rented"
        print(f'Make: {self.make}, Model: {self.model}, Status: {status}')

    def marked_rented(self):
        if self.is_available:
            self.is_available=False
            print(f'{self.make} {self.model} has been marked as rented.')
        else:
            print(f'{self.make} {self.model} is already rented.')

make = "Honda"
model = "Civik"
vehicle = Vehicle(make, model, True)
vehicle.display_info()
vehicle.marked_rented()
vehicle.display_info()