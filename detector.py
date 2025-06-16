from app.model import predict_email_phishing
import re

def find_red_flags(email_text):
    flags = []

    # Check for free domains in sender or mention of email
    if re.search(r'@(gmail|yahoo|outlook|hotmail)\.com', email_text, re.I):
        flags.append("Uses personal email domain (e.g., gmail.com)")

    # Urgent or threatening language
    if re.search(r'\b(urgent|immediately|asap|act now|verify)\b', email_text, re.I):
        flags.append("Uses urgent or threatening language")

    # Promises like winning money or job offers
    if re.search(r'\b(congratulations|win|hiring|internship|offer)\b', email_text, re.I):
        flags.append("Mentions rewards, job offers, or prizes")

    # Any mention of clicking links
    if re.search(r'\b(click here|link|http[s]?:\/\/)\b', email_text, re.I):
        flags.append("Mentions clicking suspicious links")

    # Generic sender (no real identity)
    if re.search(r'\b(team|support|hr)\b', email_text, re.I):
        flags.append("Sender name is vague or generic")

    return flags


def detect_email(email_text):
    label, confidence = predict_email_phishing(email_text)
    red_flags = find_red_flags(email_text)

    result = {
        "classification": "Phishing" if label == 1 else "Legitimate",
        "confidence": confidence,
        "red_flags": red_flags
    }
    return result
