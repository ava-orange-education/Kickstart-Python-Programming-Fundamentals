# Define the list of favorite movies 
favorite_movies = ['Inception', 'The Matrix', 'Interstellar'] 
# Function to check and update movie list 
def check_movie(movie_name): 
    if movie_name in favorite_movies: 
        print("That's one of my favorites too!") 
    else: 
        favorite_movies.append(movie_name) 
        print("I haven't seen that one, but I'll check it out!") 

# Test the function 
check_movie('The Matrix') 
check_movie('Avatar')