from Web_scrapper_LH import scrape_local_html , text_content
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

print(tokenizer)

def predict_sentiment(text):
    try:
        # Tokenize the input text
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

# Predict sentiment
predicted_sentiment_class = predict_sentiment(text_content)



if predicted_sentiment_class == 1: 
    hahah = "Very Bad"
elif predicted_sentiment_class == 2: 
    hahah = "Bad"
elif predicted_sentiment_class == 3: 
    hahah = "Average"
elif predicted_sentiment_class == 4: 
    hahah = "Good"
else: 
    hahah = "Very Good" 




if predicted_sentiment_class is not None:
    print("Predicted sentiment class:", hahah)
else:
    print("Failed to predict sentiment.")
