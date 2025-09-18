from transformers import pipeline

# Load Hugging Face emotion classification model
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

# Extra keywords for Gen Z + classic emotions
extra_emotions = {
    "shook": "surprise",
    "salty": "anger",
    "lit": "joy",
    "simp": "love",
    "mood": "relatable",
    "vibe": "calm",
    "lowkey": "secretive",
    "highkey": "intense",
    "sus": "suspicion",
    "ghosted": "sadness",
    "canceled": "disgust",
    "flex": "pride"
}

def emotion_predictor(text):
    """
    Advanced emotion detector combining transformer model and extra keywords.
    Returns top 3 emotions with scores.
    """
    text_lower = text.lower()

    # 1️⃣ Get Hugging Face model predictions
    results = emotion_model(text)[0]  # returns list of dicts
    emotions = {res["label"]: round(res["score"], 3) for res in results}

    # 2️⃣ Add extra emotion keywords
    for word, mapped_emotion in extra_emotions.items():
        if word in text_lower:
            if mapped_emotion in emotions:
                emotions[mapped_emotion] += 0.2
            else:
                emotions[mapped_emotion] = 0.2

    # 3️⃣ Cap all values at 1.0
    for key in emotions:
        if emotions[key] > 1.0:
            emotions[key] = 1.0

    # 4️⃣ Keep only top 3 emotions
    top_emotions = dict(
        sorted(emotions.items(), key=lambda x: x[1], reverse=True)[:3]
    )

    return {
        "input_text": text,
        "predicted_emotions": top_emotions
    }


# -----------------------------
# Test the function
# -----------------------------
if __name__ == "__main__":
    test_sentences = [
        "I am so happy and excited today!",
        "I am scared and nervous about my exams.",
        "I feel sad and lonely.",
        "This food is disgusting and gross.",
        "I am frustrated and angry with this situation.",
        "I love how amazing this day feels!",
        "I feel nostalgic thinking about my childhood.",
        "That party was lit and everyone was shook!",
        "She ghosted me and I feel salty.",
        "He was flexing on everyone, highkey impressive."
    ]

    for sentence in test_sentences:
        result = emotion_predictor(sentence)
        print(f"Input: {sentence}")
        print("Top Emotions:")
        for emotion, score in result["predicted_emotions"].items():
            print(f"  {emotion}: {score}")
        print("-" * 60)
