class Car: 
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year 
    def display_info(self): 
        return f"{self.year} {self.make} {self.model}" 
# Creating an instance of Car 
my_car = Car("Toyota", "Corolla", 2021) 
print(my_car.display_info()) # Outputs: 2021 Toyota Corolla 
