import re
from collections import Counter

def analyze_text(text):
    # Basic String Operations
    words = text.split()
    num_words = len(words)
    num_characters = len(text)
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    
    # String Methods
    word_frequencies = Counter(words)
    most_common_word = word_frequencies.most_common(1)[0][0]
    
    # Regular Expressions
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    
    # String Formatting
    report = (
        f"Text Analysis Report:\n"
        f"{'-'*20}\n"
        f"Number of words: {num_words}\n"
        f"Number of characters: {num_characters}\n"
        f"Number of sentences: {num_sentences}\n"
        f"Most frequent word: {most_common_word}\n"
        f"Email addresses found: {', '.join(emails) if emails else 'None'}\n"
    )
    return report

def main():
    user_text = input("Enter a block of text:\n")
    analysis_report = analyze_text(user_text)
    print(analysis_report)

if __name__ == "__main__":
    main()
