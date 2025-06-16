# Phishing-Mail-Detection
📌 Project Title:
ML-Based Phishing Email Detector Using Flask
🧠 Project Overview:
This project is a web-based application that uses a Machine Learning model to detect whether a given email is phishing or legitimate. The system also highlights red flags found in the email content to help users understand what makes an email suspicious.

🧮 Core Algorithm Used:
✅ Random Forest Classifier
A popular supervised learning algorithm used for classification.

It builds multiple decision trees and merges them to get a more accurate and stable prediction.

Performs well with text classification when converted to numerical vectors.

🔍 Feature Extraction:
✅ TF-IDF Vectorizer (from sklearn.feature_extraction.text)
Converts email text into numerical form.

Measures how important a word is to a document in a collection (Term Frequency – Inverse Document Frequency).

Filters out common, irrelevant words and gives weight to unique, meaningful ones.

🗂 Project Modules:
1. ml/phishing_model.pkl
The trained Random Forest model serialized using joblib.

2. ml/vectorizer.pkl
The trained TF-IDF vectorizer, also saved using joblib.

3. app/model.py
Loads the model and vectorizer.

Exposes a function predict_email_phishing() that returns classification and confidence score.

4. app/detector.py
Contains logic for phishing detection.

Also includes red flag detection, e.g. urgent phrases, suspicious domains, fake offers, etc.

5. main.py
Main Flask app that defines routes and connects backend to frontend.

6. templates/index.html
Simple HTML interface to enter/paste email content and see results.

🧠 How It Works (Flow):
User inputs email content via web form.

The content is passed to the detect_email() function.

This function:

Uses the vectorizer to convert text to a numeric format.

Uses the Random Forest model to predict:

Label → Phishing (1) or Legitimate (0)

Confidence score (probability)

Applies red flag detection on the text using regex.

The results (label, confidence, red flags) are shown to the user on the webpage.

🧰 Libraries & Tools Used:
Library	Purpose
Flask	Web framework for building the UI and backend
scikit-learn	ML model and TF-IDF vectorizer
joblib	For loading and saving the model/vectorizer
re	Regular expressions for detecting red flags
HTML/CSS	Frontend form and result rendering

💡 Red Flag Detection Logic:
Regex-based checks for:

🚩 Use of personal email domains (@gmail.com, etc.)

🚩 Urgent/commanding words: urgent, immediately, act now

🚩 Rewards: win, congratulations, hiring

🚩 Links: presence of http, click here

🚩 Generic sender names: support, team, HR

✅ Output Includes:
✔ Classification: Phishing / Legitimate

📊 Confidence Score: %

🛑 List of Red Flags

🧪 Improvements You Can Add:
Allow email uploads (.eml/.txt)

Save history in SQLite or CSV

Add sender email domain extraction

Highlight suspicious words directly in email body

Train a deep learning model (LSTM or BERT) for improved accuracy
