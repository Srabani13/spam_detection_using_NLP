# Import necessary libraries
# Flask for web app development
# Flask is a lightweight web application framework for Python. It allows you to create web applications quickly and easily.
from flask import Flask, request, jsonify 
# For loading the pre-trained model
import pickle  
# TF-IDF Vectorizer for text feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer 
# For text preprocessing (regular expressions)
import re  
# For natural language processing tasks
import nltk  
# For removing common stopwords
from nltk.corpus import stopwords  
# For tokenizing text into words
from nltk.tokenize import word_tokenize  
# For stemming words to their root form
from nltk.stem import PorterStemmer  


# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()



# Load the pre-trained machine learning models
with open("rf_model.pkl", "rb") as model_file:
    rf_model = pickle.load(model_file)

with open("rf_model.pkl", "rb") as model_file:
    rf_model = pickle.load(model_file)


# Define a function for text preprocessing
"""
Preprocess the input text for machine learning predictions.

Steps:
1. Convert text to lowercase.
2. Remove HTML tags, special characters, and punctuation.
3. Tokenize the text into words.
4. Remove non-alphanumeric tokens (special characters, numbers, etc.).
5. Remove common stopwords.
6. Stem words to their root form.
7. Recombine tokens into a single cleaned string.

Parameters:
    text (str): The input raw text.

Returns:
    clean_text (str): The preprocessed and cleaned text.
"""


# Define a function for text preprocessing
def preprocess_text(text):
    text = text.lower()  # Convert text to lowercase
    text = re.sub(r".*?>"'', text) ## Remove HTML tags and other non-alphanumeric characters using regex

    # Tokenize the text into individual words
    token = word_tokenize(text)

    # Remove punctuation and special characters
    clean_token = [word for word in token if word.isalnum()]

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in token if token.lower() not in stop_words]

    # Stem words to their root forms
    ps = PorterStemmer()
    stemmed_tokens = [ps.stem(token) for token in filtered_tokens]

    # Combine the cleaned and stemmed tokens into a single string
    clean_text =' '.join(stemmed_tokens)
    return clean_text


# Initialize Flask application
app = Flask(__name__)
@app.route("/predict", methods=["POST"])

# Define a function for making predictions
def predict():
    message = request.json["message"]

    preprocess_text = preprocess_text(message)

    vectorizer_message = tfidf_vectorizer.transform([preprocess_text])

    prediction = rf_model.predict(vectorizer_message)

    # Return the prediction as a JSON response
    return jsonify({"prediction": prediction[0]})

# Run the Flask application
if __name__ == "__main__":
    # Run the application on host "0.0.0.0" and port 5000 with debug mode enabled
    app.run(host="0.0.0.0", port= 5000, debug=True)