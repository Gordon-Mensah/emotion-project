# Emotion Detection Project 🎭

A Python project that detects emotions from text using **Natural Language Processing (NLP)**.
The application can be run as a console program or deployed as a Flask-based web application.

---

## ✨ Features

* Detects multiple emotions such as:

  * Joy 😊
  * Sadness 😢
  * Anger 😡
  * Fear 😨
  * Disgust 🤢
  * And more, using advanced NLP models
* Includes unit tests to validate functionality
* Error handling for invalid or empty inputs
* Flask web application for easy deployment
* Static code analysis ready (pylint compliance)

---

## 🛠️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Gordon-Mensah/emotion-project.git
   cd emotion-project
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate      # On Windows
   source .venv/bin/activate     # On Mac/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### Run Emotion Detector (console mode)

```bash
python emotions_app.py
```

### Run Flask Web Application

```bash
python server.py
```

Then open your browser at:
👉 `http://127.0.0.1:5000`

---

## ✅ Running Tests

Unit tests are included under the `tests/` folder.
Run them with:

```bash
pytest tests/
```

---

## 📂 Project Structure

```
emotion-project/
│── emotion_detector/
│   ├── __init__.py
│   ├── emotion.py
│── tests/
│   ├── test_emotion.py
│── emotions_app.py
│── server.py
│── requirements.txt
│── README.md
```

---

## 📊 Static Code Analysis

To check code quality with **pylint**:

```bash
pylint emotion_detector emotions_app.py server.py
```

---

## 📜 License

This project is licensed under the MIT License.
Feel free to use and modify for your own projects!

---

## 👨‍💻 Author

**Gordon Mensah**
🔗 [GitHub Profile](https://github.com/Gordon-Mensah)

