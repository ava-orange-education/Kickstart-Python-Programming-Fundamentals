def capitalize_words(s):
    """Capitalize each word in the string."""
    return ' '.join(word.capitalize() for word in s.split())