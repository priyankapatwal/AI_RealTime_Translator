import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

def capture_speech():
    try:
        # Use the microphone as input
        with sr.Microphone() as source:
            print("Listening...")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            # Record audio from the user
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            # Convert speech to text
            text = recognizer.recognize_google(audio)
            print(f"Captured Text: {text}")
            return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Speech Recognition service; {e}")
        return None
        
        
from googletrans import Translator

# Initialize the translator
translator = Translator()

def translate_text(text, target_language="es"):
    try:
        # Translate the input text
        translated = translator.translate(text, dest=target_language)
        print(f"Translated Text: {translated.text}")
        return translated.text
    except Exception as e:
        print(f"Translation Error: {e}")
        return None

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    try:
        # Analyze sentiment
        scores = sentiment_analyzer.polarity_scores(text)
        compound_score = scores['compound']

        # Determine sentiment category
        if compound_score > 0.05:
            sentiment = "Positive"
        elif compound_score < -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        print(f"Sentiment Analysis: {sentiment} (Score: {compound_score})")
        return sentiment
    except Exception as e:
        print(f"Sentiment Analysis Error: {e}")
        return None

                
import pyttsx3

# Initialize the text-to-speech engine
tts = pyttsx3.init()

# Set TTS properties (optional)
tts.setProperty('rate', 150)  # Speed of speech
tts.setProperty('volume', 1)  # Volume (0.0 to 1.0)

def text_to_speech(text):
    try:
        print("Speaking the text...")
        tts.say(text)
        tts.runAndWait()
    except Exception as e:
        print(f"TTS Error: {e}")

if __name__ == "__main__":
    # Test the full pipeline
    print("Press Enter to start recording (or type 'exit' to quit):")
    while True:
        command = input().strip()
        if command.lower() == "exit":
            break

        captured_text = capture_speech()
        if captured_text:
            translated_text = translate_text(captured_text, target_language="es")
            if translated_text:
                sentiment = analyze_sentiment(captured_text)
                # Combine translated text and sentiment for TTS
                speech_output = f"Translation: {translated_text}. Sentiment: {sentiment}."
                text_to_speech(speech_output)


