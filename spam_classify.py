from flask import Flask, request, jsonify
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

# Load pre-trained models
with open("rf_model.pkl", "rb") as model_file:
    rf_model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    tfidf_vectorizer = pickle.load(vectorizer_file)

app = Flask(__name__)

# Preprocessing function
def preprocess_text(text):
    if isinstance(text, list):
        text = ' '.join([t.lower() for t in text])
    else:
        text = text.lower()
    
    text = re.sub(r"http\S+|www\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)       # Remove special characters and numbers
    
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    clean_text = ' '.join(lemmatized_tokens)
    return clean_text

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    messages = data.get("message", [])

    if not isinstance(messages, list):
        messages = [messages]

    preprocessed_messages = [preprocess_text(msg) for msg in messages]
    vectorized_messages = tfidf_vectorizer.transform(preprocessed_messages)
    predictions = rf_model.predict(vectorized_messages)

    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
