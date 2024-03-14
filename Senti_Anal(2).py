from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer  # For negation handling

# Load tokenizer and model (same as before)
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def predict_sentiment(text):
  try:
    # Preprocess text (lowercase, remove punctuation, negation handling)
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation

    # NLTK Vader for basic negation handling (optional)
    vader = SentimentIntensityAnalyzer()
    sentiment = vader.polarity_scores(text)
    negated = sentiment['neg'] > 0.5  # Check for strong negation

    if negated:
      # Reverse sentiment if negation is detected (basic approach)
      text = f"NOT {text}"

    # Tokenize the processed text
    tokens = tokenizer(text, return_tensors='pt')

    # Pass the tokens to the model for prediction
    result = model(**tokens)

    # Extract the logits and predict the sentiment class
    logits = result.logits
    predicted_class_index = torch.argmax(logits)
    predicted_sentiment_class = int(predicted_class_index) + 1

    return predicted_sentiment_class
  except Exception as e:
    print("Error occurred during prediction:", e)
    return None

# Get input text from the user
user_input = input("Enter the text you want to perform sentiment analysis on: ")

# Predict sentiment
predicted_sentiment_class = predict_sentiment(user_input)

sentiment_map = {
    1: "Very Negative",
    2: "Negative",
    3: "Neutral",
    4: "Positive",
    5: "Very Positive"
}

predicted_sentiment = sentiment_map.get(predicted_sentiment_class)

if predicted_sentiment:
  print(f"Predicted Sentiment: {predicted_sentiment}")
else:
  print("Error: Could not predict sentiment.")

