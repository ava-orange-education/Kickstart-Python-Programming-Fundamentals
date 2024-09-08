# Definition of classes for three everyday objects 
class Chair: 
    def __init__(self, material, height): 
        self.material = material 
        self.height = height 
    def adjust_height(self, new_height): 
        self.height = new_height 

class Phone: 
    def __init__(self, brand, model): 
        self.brand = brand 
        self.model = model 
    def make_call(self, number): 
        print(f"Calling {number}...") 

class Lamp: 
    def __init__(self, color, brightness): 
        self.color = color 
        self.brightness = brightness 
    def change_brightness(self, new_brightness): 
        self.brightness = new_brightness 

# Test the code 
office_chair = Chair('leather', 120) 
office_chair.adjust_height(125) 
print(f"Adjusted chair height to {office_chair.height}cm") 

mobile_phone = Phone("Apple", "iPhone 13") 
mobile_phone.make_call("1234567890") 

study_lamp = Lamp("white", 75) 
study_lamp.change_brightness(80) 

print(f"Lamp brightness set to {study_lamp.brightness}%")