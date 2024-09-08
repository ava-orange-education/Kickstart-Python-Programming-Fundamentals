def count_vowels(s):
    """Count the number of vowels in the string."""
    return sum(1 for char in s if char.lower() in 'aeiou')