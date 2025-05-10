from transformers import pipeline

# Cache the model to avoid reloading
emotion_model = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", return_all_scores=True)

def analyze_emotion(text):
    scores = emotion_model(text)[0]
    top_emotion = max(scores, key=lambda x: x["score"])
    return top_emotion["label"], round(top_emotion["score"], 2)