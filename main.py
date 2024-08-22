import cv2
from deepface import DeepFace
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='your_client_id',
                                                           client_secret='your_client_secrets'))

def analyze_emotion(frame):
    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    
    # If the result is a list (multiple faces detected), use the first one
    if isinstance(result, list):
        result = result[0]
    
    return result['dominant_emotion']

def recommend_song(emotion,last_emotion):
    # Define a basic mapping from emotion to song genre or mood
    emotion_to_genre = {
        'happy': 'happy',
        'angry': 'angry',
        'sad': 'sad',
        'surprise': 'surprise',
        'neutral': 'calm'
    }
    
    genre = emotion_to_genre.get(emotion, 'calm')
    
    # Search for a song in the chosen genre
    results = sp.search(q=f'genre:{genre}', type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track['name'], track['artists'][0]['name']
    return 'No song found', ''

def main():
    cap = cv2.VideoCapture(0)
    
    # Create a named window
    window_name = "Emotion Analysis"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # Resize the window to be larger horizontally
    cv2.resizeWindow(window_name, 800, 400)

    frame_skip = 4  # Process every 4th frame
    frame_count = 0
    
    last_emotion = None  # Initialize last emotion tracker
    song_name = 'No song found'
    artist_name = ''

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        if frame_count % frame_skip != 0:
            # Skip this frame to reduce lag
            continue

        emotion = analyze_emotion(frame)
        
        # Only fetch a new song if the emotion has changed
        if emotion != last_emotion:
            song_name, artist_name = recommend_song(emotion, last_emotion)
            last_emotion = emotion
        
        # Display the emotion and song recommendation on the frame
        cv2.putText(frame, f'Emotion: {emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f'Song: {song_name}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f'Artist: {artist_name}', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
        
        # Show the frame in the larger window
        cv2.imshow(window_name, frame)
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

