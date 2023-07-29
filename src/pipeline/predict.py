# Models
from deepface import DeepFace
from transformers import pipeline

# OCR
import pytesseract

# Custom
from src.logger import logging

class Predict:
    def __init__(self):
        pass

    def predict_with_pretrained(self, X_input):
        """This functions detects the dominant emotion in the given image
        Args:
            X_input (str): path of the image
        Returns:
            str: detected emotion
        """
        
        # Try Block to detect emotion if image contains a face and throws exception if no face is detected in the image
        try:
            pred = DeepFace.analyze(img_path=X_input, actions=('emotion'), enforce_detection=True)[0]['dominant_emotion'].capitalize()
            logging.info('Face Detected')
            logging.info(f'Emotion: {pred}')
        # Exception Block to detect the emotion in the text
        except:
            logging.info('No face detected')
            # Performing OCR to extract the text from the image
            logging.info('Initializing text detection')
            text = pytesseract.image_to_string(X_input)
            # if no text is found in the image
            if text == '':
                pred = 'The image does not contain any face or text'
            # Detecting the emotion in the found text
            else:
                logging.info('Text detected')
                classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
                pred = classifier(text)[0]['label'].capitalize()
                logging.info(f'Emotion: {pred}')
        return pred
