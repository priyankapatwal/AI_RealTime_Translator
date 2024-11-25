from flask import Flask, request, jsonify, render_template
import speech_recognition as sr
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pyttsx3

app = Flask(__name__)

# Initialize components
recognizer = sr.Recognizer()
translator = Translator()
sentiment_analyzer = SentimentIntensityAnalyzer()

# Text-to-Speech
tts = pyttsx3.init()
tts.setProperty('rate', 150)
tts.setProperty('volume', 1.0)

def capture_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        return recognizer.recognize_google(audio)

def translate_text(text, target_language="es"):
    return translator.translate(text, dest=target_language).text

def analyze_sentiment(text):
    scores = sentiment_analyzer.polarity_scores(text)
    compound_score = scores['compound']
    if compound_score > 0.05:
        return "Positive"
    elif compound_score < -0.05:
        return "Negative"
    else:
        return "Neutral"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        captured_text = capture_speech()
        translated_text = translate_text(captured_text)
        sentiment = analyze_sentiment(captured_text)
        return jsonify({
            'captured_text': captured_text,
            'translated_text': translated_text,
            'sentiment': sentiment
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
