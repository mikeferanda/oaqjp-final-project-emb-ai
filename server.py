"""A Flask application for performing emotion detection on text input."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector  # First party import

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    """Renders the index.html page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def analyze_emotion():
    """
    Analyzes the emotion of the text provided in the request.

    Returns:
        str: A formatted string containing the emotion analysis results,
             or an error message for invalid input.
    """
    if request.method == 'POST':
        text_to_analyze = request.form['textToAnalyze']
        emotion_result = emotion_detector(text_to_analyze)

        if emotion_result:
            anger = emotion_result.get('anger')
            disgust = emotion_result.get('disgust')
            fear = emotion_result.get('fear')
            joy = emotion_result.get('joy')
            sadness = emotion_result.get('sadness')
            dominant_emotion = emotion_result.get('dominant_emotion')

            if dominant_emotion is None:
                return "Invalid text! Please try again!"
            formatted_response = (
                f"For the given statement, the system response is "
                f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
                f"'joy': {joy} and 'sadness': {sadness}. "
                f"The dominant emotion is {dominant_emotion}."
            )
            return formatted_response
        return "Error analyzing emotion."
    return "Invalid request method"

if __name__ == '__main__':
    app.run(debug=True)
    
