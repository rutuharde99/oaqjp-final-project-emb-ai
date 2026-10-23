```python
import json
import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(
        url,
        headers=headers,
        json={"raw_document": {"text": text_to_analyze}}
    )

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion
        }

    elif response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
```

**File name:** `2a_emotion_detection.py`

**Note:** हा code expected Watson NLP response structure वर आधारित आहे. Coursera lab मध्ये दिलेली exact API URL आणि response structure वेगळी असल्यास lab मधील code वापर. Code save करून मग Coursera च्या instructions प्रमाणे submit कर.
