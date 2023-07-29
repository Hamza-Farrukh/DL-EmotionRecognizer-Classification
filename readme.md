# Emotion Recognizer
Emotion Recognizer is a desktop application developed using Flaskwebgui and Django frameworks. The project aims to analyze images and text to recognize emotions expressed by individuals. It utilizes deep learning algorithms for facial expression analysis and a pre-trained model for emotion detection in text.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features
- User Registration and Login: New users can create an account and registered users can log in securely.
- Image Emotion Recognition: Users can upload images with human faces expressing emotions for analysis.
- Text Emotion Recognition: The application extracts text from images and detects emotions within the text.
- User-friendly Interface: The application provides a user-friendly interface for seamless interaction.

## Installation
1. Clone the repository to your local machine.
2. Install the required dependencies using the following command:  
pip install -r requirements.txt
3. Set up the database and perform migrations:  
python manage.py makemigrations  
python manage.py migrate
4. Start the development server:  
python manage.py runserver
5. Start the GUI using the following command:   
python EmotionRecognizer.py

## Usage
1. Open your web browser and navigate to the local server address provided after starting the development server.
2. If you are a new user, click on "Sign Up" to create an account. Otherwise, log in using your credentials.
3. On the home page, you can upload an image for emotion recognition or input text within an image.
4. The application will process the image or text and display the recognized emotions.

## Technologies Used
- Flaskwebgui
- Django
- PyInstaller
- jQuery
- HTML
- CSS
- Bootstrap
- Visual Studio Code (VSCode)
- deepface
- pytesseract
- j-hartmann/emotion-english-distilroberta-base model

## Contributing
Contributions to the Emotion Recognizer project are welcome. Please fork the repository and create a pull request for your contributions.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code as per the terms of the license.
