# Define the dictionary of continents and countries 
world = {'Asia': ['China', 'India', 'Japan'], 'Europe': ['France', 'Germany', 'Italy']} 
# Function to display countries in a continent 
def display_countries(continent): 
    countries = world.get(continent, "Continent not found") 
    if type(countries) is list: 
        print("Countries in", continent + ":", ', '.join(countries)) 
    else: 
        print(countries) 
# Test the function 
display_countries('Asia') 
display_countries('Africa') 