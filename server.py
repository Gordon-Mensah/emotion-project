from flask import Flask, request, jsonify, render_template
from emotion_detector.emotion import emotion_predictor

app = Flask(__name__)

# Home route: simple form to input text
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form.get("text", "")
        if not text.strip():
            return render_template("index.html", error="Please enter some text!")
        result = emotion_predictor(text)
        return render_template("index.html", result=result, input_text=text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
