import re

#Matching Digits: \d
#Matches any digit (0-9).
pattern = r"\d+"
text = "The year is 2024"
matches = re.findall(pattern, text)
print("Digits found:", matches)  # ['2024']

#Matching Word Characters: \w
#Matches any word character (alphanumeric + underscore).
pattern = r"\w+"
text = "Hello, world!"
matches = re.findall(pattern, text)
print("Words found:", matches)  # ['Hello', 'world']

#Matching Whitespace: \s
#Matches any whitespace character (spaces, tabs, newlines).
pattern = r"\s+"
text = "Hello   world"
matches = re.findall(pattern, text)
print("Whitespace found:", matches)  # ['   ']

#Matching Start and End of String: ^ and $
#^ matches the start of the string.
#$ matches the end of the string.
pattern = r"^hello"
text = "hello world"
if re.match(pattern, text):
    print("String starts with 'hello'")

pattern = r"world$"
if re.search(pattern, text):
    print("String ends with 'world'")

#Matching a Specific Number of Repetitions: {m,n}
#Matches between m and n repetitions of the preceding character.
pattern = r"\d{2,4}"
text = "2024"
matches = re.findall(pattern, text)
print("Matches with 2 to 4 digits:", matches)  # ['2024']
