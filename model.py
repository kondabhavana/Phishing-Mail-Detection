import joblib
import os

# Load model and vectorizer
MODEL_PATH = os.path.join("ml", "phishing_model.pkl")
VECTORIZER_PATH = os.path.join("ml", "vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def predict_email_phishing(email_text):
    vect = vectorizer.transform([email_text])
    prediction = model.predict(vect)[0]
    probability = model.predict_proba(vect)[0][prediction]
    return prediction, round(probability * 100, 2)
