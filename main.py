from flask import Flask, render_template, request
from app.detector import detect_email

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        email_content = request.form.get('email_content', '')
        result = detect_email(email_content)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
