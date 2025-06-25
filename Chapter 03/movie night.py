# Conditions for movie night 
have_enough_snacks = True 
weather_is_clear = False 
# Using logical operators to decide if movie night can happen 
can_have_movie_night = have_enough_snacks and weather_is_clear 
# Using the 'not' operator to check if movie night cannot proceed 
cannot_have_movie_night = not can_have_movie_night 
print(f"Can we have movie night? {can_have_movie_night}") 
print(f"Cannot have movie night? {cannot_have_movie_night}")