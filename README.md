# Song-recomendation-via-Sentiment-Analysis

Emotion-Based Music Recommendation with OpenCV and Spotify

This project uses OpenCV for face detection and emotion recognition, and Spotify's API to recommend music based on your current emotion.
Features

    Analyzes your emotions through your webcam.
    Recommends songs based on a basic emotion-to-genre mapping.
    Displays the detected emotion and recommended song on the webcam feed.

Requirements

    Python 3.x
    OpenCV (cv2)
    DeepFace
    Spotipy

Installation:

Read How-to.txt to get the full installation support. xoxo.

Spotify API Credentials:

You will need to obtain a Spotify Developer account and create an app to get your client ID and client secret. Replace 'your_client_id' and 'your_client_secrets' in the code with your own credentials.
Running the Project

    Save the code as main.py.
    Open a terminal in the project directory.
    Run the script:


python3 main.py

Use code with caution.

    The script will open your webcam and analyze your emotions in real-time, recommending songs based on the detected emotion. Press 'q' to quit.

How it Works

    The script initializes OpenCV to capture video from your webcam.
    It uses DeepFace to analyze the emotions in each frame.
    A basic mapping between emotions and genres is defined (e.g., happy -> happy music).
    Spotipy is used to search for a song in the chosen genre.
    The detected emotion and recommended song are displayed on the webcam feed.
    The script skips frames to reduce processing load.

Note: This is a basic implementation and can be further improved by:

    Expanding the emotion-to-genre mapping for more nuanced recommendations.
    Adding logic to handle situations where no song is found.
    Integrating with a music player to automatically play the recommended song.

This README provides a basic understanding of the project. Feel free to explore the code and contribute to its development!
