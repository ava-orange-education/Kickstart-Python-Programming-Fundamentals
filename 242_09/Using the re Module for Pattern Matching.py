import re

#re.search(): Looks for the first instance of the pattern in the string. Returns a match object if found; else returns None.

pattern = r"hello"
text = "hello world"
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")

#re.match(): Checks whether the pattern matches the beginning of the string. Returns a match object if found; else returns None.
match = re.match(pattern, text)
if match:
    print("Match found at the beginning:", match.group())
else:
    print("No match found at the beginning")

#re.findall(): Returns a list of all non-overlapping matches for the pattern in the string.
text = "hello world, hello universe"
matches = re.findall(pattern, text)
print("All matches:", matches)  # ['hello', 'hello']

#re.sub(): Replaces every occurrence of the pattern in the string with the provided replacement.
text = "hello world"
new_text = re.sub(pattern, "hi", text)
print("Replaced text:", new_text)  # 'hi world'

#re.split(): Splits the string based on pattern occurrences and returns a list of substrings.
text = "hello world, hello universe"
parts = re.split(r"\s", text)
print("Splitted text:", parts)  # ['hello', 'world,', 'hello', 'universe']
