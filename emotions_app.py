from transformers import pipeline

# Load a HuggingFace model for emotion detection
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

def emotion_predictor(text):
    """
    Advanced emotion predictor using HuggingFace Transformers.
    Returns structured output with scores for multiple emotions.
    """
    results = emotion_pipeline(text)

    # Convert list of dicts into a cleaner structure
    emotions = {item['label']: round(item['score'], 4) for item in results[0]}

    return {
        "input_text": text,
        "predicted_emotions": emotions
    }

# -----------------------------
# Test the function
# -----------------------------
if __name__ == "__main__":
    test_sentences = [
        "I am so happy and excited today!",
        "I'm anxious about my exams tomorrow.",
        "That was disgusting and gross!",
        "I'm feeling nostalgic and a bit lonely.",
        "This game is absolutely lit, I love it!"
    ]

    for sentence in test_sentences:
        result = emotion_predictor(sentence)
        print(f"Input: {sentence}")
        print(f"Predicted Emotions: {result}")
        print("-" * 40)
