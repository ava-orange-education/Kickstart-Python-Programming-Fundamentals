# Import the string manipulation modules from the string_tools package 
from string_tools.reverse import reverse_string 
from string_tools.capitalize import capitalize_words 
from string_tools.count_vowels import count_vowels 
# Test the string manipulation functions with a sample text 
sample_text = "hello world" 
# Reverse the text using the reverse_string function 
reversed_text = reverse_string(sample_text) 
print(f"Reversed Text: {reversed_text}") 
# Capitalize the text using the capitalize_words function 
capitalized_text = capitalize_words(sample_text) 
print(f"Capitalized Text: {capitalized_text}") 
# Count the number of vowels in the text using the count_vowels function 
vowel_count = count_vowels(sample_text) 
print(f"Number of vowels: {vowel_count}")