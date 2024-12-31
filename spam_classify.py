from flask import Flask, request, jsonify 
import pickle  
from sklearn.feature_extraction.text import TfidfVectorizer 
import re  
import nltk  
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
from nltk.stem import PorterStemmer  

# Load the pre-trained machine learning models
with open("rf_model.pkl", "rb") as model_file:
    rf_model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as model_file:
    tfidf_vectorizer = pickle.load(model_file)

# Define a function for text preprocessing
def preprocess_text(text):
    if isinstance(text, list):
        text = ' '.join([t.lower() for t in text])
    else:
        text = text.lower()
    text = re.sub(r".*?>", '', text)

    tokens = word_tokenize(text)
    clean_tokens = [word for word in tokens if word.isalnum()]

    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in clean_tokens if token.lower() not in stop_words]

    ps = PorterStemmer()
    stemmed_tokens = [ps.stem(token) for token in filtered_tokens]

    clean_text = ' '.join(stemmed_tokens)
    return clean_text

# Initialize Flask application
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    message = data.get("message")
    preprocessed_text = preprocess_text(message)

    vectorized_message = tfidf_vectorizer.transform([preprocessed_text])
    prediction = rf_model.predict(vectorized_message)

    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
