import math 
def calculate_area(radius): 
    return math.pi * radius ** 2 

def main(): 
    user_input = input("Enter the radius of the circle: ") 
    radius = float(user_input) 
    area = calculate_area(radius) 
    print(f"The area of the circle with radius {radius} is: {area:.2f}") 

if __name__ == "__main__": main()
