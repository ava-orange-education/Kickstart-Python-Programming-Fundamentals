# Define the dictionary 
programming_languages = {'Python': 'Guido van Rossum', 'Java': 'James Gosling'} 
# Function to get creator 
def get_creator(language): 
    return programming_languages.get(language, "Unknown language") 
# Update dictionary if unknown 
def update_language(language, creator): 
    if get_creator(language) == "Unknown language": 
        programming_languages[language] = creator 
        print(f"Added {language} created by {creator} to the dictionary.") 
    else: 
        print(f"{language} was created by {get_creator(language)}.") 
# Test the function 
print(get_creator('Python')) 
update_language('Ruby', 'Yukihiro Matsumoto')