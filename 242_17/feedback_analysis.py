import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('./data/customer_feedback_sample.csv')

# Clean the data
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())  # Handle missing ratings
df = df.drop_duplicates()  # Remove duplicate feedback entries

# Analyze the data
average_rating = df['Rating'].mean()
most_common_keywords = pd.Series(' '.join(df['FeedbackText']).lower().split()).value_counts()[:10]

# Group and aggregate the data
rating_counts = df['Rating'].value_counts()

# Visualize the data
rating_counts.plot(kind='bar', title='Distribution of Ratings')
plt.figure(figsize=(10, 6))
wordcloud = WordCloud().generate(' '.join(df['FeedbackText']))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Display results
print(f"Average Rating: {average_rating}")
print("Most Common Keywords:")
print(most_common_keywords)
