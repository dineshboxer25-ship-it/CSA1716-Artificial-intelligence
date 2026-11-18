# Sentiment Analysis using NLP

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample dataset
texts = [
    "I love this product",
    "This is an amazing experience",
    "The movie is very good",
    "I am happy with the service",
    "This product is excellent",
    "I hate this product",
    "This is a terrible experience",
    "The movie is very bad",
    "I am unhappy with the service",
    "This product is worst"
]

labels = [
    "Positive", "Positive", "Positive",
    "Positive", "Positive",
    "Negative", "Negative", "Negative",
    "Negative", "Negative"
]

# Convert text into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Create and train model
model = MultinomialNB()
model.fit(X, labels)

# Test sentence
sentence = ["This product is amazing"]

# Convert test sentence
test_data = vectorizer.transform(sentence)

# Predict sentiment
prediction = model.predict(test_data)

print("Sentiment Analysis using NLP")
print("Input Text:", sentence[0])
print("Predicted Sentiment:", prediction[0])
