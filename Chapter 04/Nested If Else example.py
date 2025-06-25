# Input age rating and genre from the user.
# These inputs determine the classification and recommendations for a movie.
age_rating = input("Enter the age rating (G, PG, PG-13, R): ")
genre = input("Enter the genre (Action, Comedy, Drama, Documentary): ")

# The first level of decision-making is based on the movie's age rating.
# This determines the suitability of the movie for different audience ages.
if age_rating == "G" or age_rating == "PG":
    # Suitable for younger audiences
    print("This movie is suitable for younger audiences.")
    
    # Nested decision-making: Provide more specific feedback based on the genre,
    # tailoring the response to the type of content within the age group.
    if genre == "Action":
        print("Expect some mild action scenes.")
    elif genre == "Comedy":
        print("Prepare for laughs suitable for all ages.")
    else:
        # If the movie is neither action nor comedy, it's assumed to be family-friendly
        print("A wholesome film for family viewing.")
        
elif age_rating == "PG-13":
    # Suitable for teens and above, indicating slightly more mature content.
    print("This movie is suitable for teens and above.")
    
    # Further nested decisions provide specific guidance on content expectations
    # for the PG-13 category based on genre.
    if genre == "Action":
        print("Moderate action scenes with minimal sensitive content.")
    elif genre == "Drama":
        print("Mature themes with an emphasis on storytelling.")
    else:
        # If the genre is neither action nor drama, a general caution is provided.
        print("Some material may not be suitable for children under 13.")
        
else:
    # Indicates the movie is for adult audiences, suggesting mature or intense content.
    print("This movie is restricted to adult audiences.")
    
    # Additional nested decisions offer insights on adult-oriented films based on genre.
    if genre == "Documentary":
        print("Insightful content with mature themes.")
    else:
        # Assumes all non-documentary movies rated for adults contain mature content.
        print("Content strictly for adults.")
