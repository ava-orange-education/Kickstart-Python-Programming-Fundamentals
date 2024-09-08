class CoffeeMachine: 
    def __init__(self): 
        self.__water_level = 100 
    # Private attribute 
    def make_coffee(self, strength): 
        if strength not in ['light', 'medium', 'strong']: 
            print("Invalid strength. Choose 'light', 'medium', or 'strong'.") 
            return 
        if self.__water_level > 10: 
            self.__water_level -= 10 
            print(f"Making {strength} coffee.") 
        else: print("Refill water.") 

# Test the code 
machine = CoffeeMachine() 
machine.make_coffee('medium')