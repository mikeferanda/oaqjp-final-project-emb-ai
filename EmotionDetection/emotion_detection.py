import requests
import json

def emotion_detector(text_to_analyze):
    """
    Runs emotion detection on the provided text using the Watson NLP library.

    Args:
        text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
        dict: A dictionary containing the scores for anger, disgust, fear, joy, sadness,
              and the name of the dominant emotion, or a dictionary with None values
              if the input is blank.
    """
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()  # Raise an exception for bad status codes
        response_json = response.json()

        # Extract emotion scores
        emotion_scores = response_json.get("emotionPredictions", [{}])[0].get("emotion", {})

        anger_score = emotion_scores.get("anger", 0.0)
        disgust_score = emotion_scores.get("disgust", 0.0)
        fear_score = emotion_scores.get("fear", 0.0)
        joy_score = emotion_scores.get("joy", 0.0)
        sadness_score = emotion_scores.get("sadness", 0.0)

        # Find the dominant emotion
        emotions = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
        }
        dominant_emotion = max(emotions, key=emotions.get)

        # Construct the output dictionary
        output_dict = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

        return output_dict

    except requests.exceptions.RequestException as e:
        print(f"Error during emotion detection: {e}")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
        return None

if __name__ == '__main__':
    text = "I love this new technology."
    emotion_result = emotion_detector(text)
    if emotion_result:
        print(json.dumps(emotion_result, indent=2))
