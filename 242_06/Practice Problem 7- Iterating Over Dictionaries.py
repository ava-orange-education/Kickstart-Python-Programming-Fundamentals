# Define the dictionary 
music_genres = {'Rock': 'Bohemian Rhapsody', 'Pop': 'Thriller', 'Jazz': 'What a Wonderful World'} 
# Function to display songs by genre 
def display_songs(): 
    for genre, song in music_genres.items(): 
        print(f"In the {genre} genre, I like {song}.") 
# Test the function 
display_songs()