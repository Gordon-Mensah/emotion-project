import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from emotion_detector.emotion import emotion_predictor

from emotion_detector.emotion import emotion_predictor

def test_joy():
    result = emotion_predictor("I am very happy today!")
    assert result["predicted_emotions"]["joy"] > 0

def test_anger():
    result = emotion_predictor("I am so mad!")
    assert result["predicted_emotions"]["anger"] > 0

# Run all tests
if __name__ == "__main__":
    test_joy()
    test_anger()
    print("All tests passed!")
