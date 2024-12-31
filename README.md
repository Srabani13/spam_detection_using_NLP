# spam_detection_using_nlp
# SpamSniffer

🐶 **SpamSniffer** - A Web Application to Detect Spam Messages using Machine Learning

## Overview

SpamSniffer is a web application designed to classify SMS messages as spam or ham (not spam) using a pre-trained machine learning model. The application provides an interactive interface built with Streamlit and a backend server powered by Flask.

## Features

- **Interactive UI**: User-friendly interface to enter SMS messages and view predictions.
  ![GUI Screenshot](https://github.com/Srabani13/spam_detection_using_nlp/blob/main/GUI_ss.png)
- **Spam Detection**: Utilizes a Random Forest model with TF-IDF vectorization to classify messages.
- **Preprocessing**: Includes robust text preprocessing steps to handle various text formats.

## Requirements

- Python 3.13.1
- Flask
- Streamlit
- scikit-learn
- nltk

## Data Collection : 
The SMS Spam dataset contains over 5,572 messages labeled as either spam or ham. Here is the [Dataset](https://github.com/Srabani13/spam_detection_using_nlp/blob/main/sms-spam.csv)

## Data Cleaning and Preprocessing :
The data was cleaned by handling null and duplicate values. The data was then preprocessed by converting the text into tokens, removing special characters, stop words and punctuation, and stemming the data. The data was also converted to lowercase before preprocessing.

## Exploratory Data Analysis :
Exploratory Data Analysis was performed to gain insights into the dataset. The count of characters, words, and sentences was calculated for each message. The total difference between spam and ham and visualizations were created using bar charts, and pie charts.

## Model Comparison :
In building the spam detection model, three machine-learning algorithms were evaluated:
- Support Vector Classifier (SVC)
- Random Forest Classifier
- Logistic Regression
## Model Comparison :
Each model was assessed based on accuracy, precision, recall, and F1-score. The Random Forest Classifier was chosen because it demonstrated slightly higher accuracy compared to the other models. Here’s a quick overview of the findings:
- Support Vector Classifier (SVC): Showed competitive results but was marginally outperformed by the Random Forest Classifier.
- Random Forest Classifier: Selected for its highest accuracy and robust performance.
- Logistic Regression: Performed well, but with slightly lower accuracy.

**The Random Forest Classifier was trained, fine-tuned, and used in the application for its balanced precision and recall, making it the best fit for detecting spam messages.**

## Deployment :
The model was deployed on the web using Streamlit. The user interface has a simple input box where the user can input a message, and the model will predict whether it is spam or not spam.


## Installation
**To use the SMS Spam Detection model on your machine**, **follow these steps:**
-  **Clone the Repository**:
```
git clone https://github.com/Srabani13/spam_detection_using_nlp.git
 ```
- **Start the Flask Server**
- Run the Flask Application:
```
python spam_classify.py
```
- Run the Streamlit Application
```
streamlit run app.py
```


## Contributions :
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request in this repository.
