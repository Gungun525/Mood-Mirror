Mood Mirror
Mood Mirror is an AI-powered web application that detects your facial emotion from a selfie and provides uplifting suggestions such as happy songs, motivational quotes, and feel-good movies to brighten your mood.

Features
Detects facial emotions using AI (DeepFace).

Provides randomized uplifting quotes, songs (with YouTube links), and movies (with IMDb links).

Simple, user-friendly interface.

No user data or images are stored.

Technologies Used
Python 3.x

Flask (Web framework)

DeepFace (Emotion detection)

HTML, CSS, Bootstrap (Frontend)

# Mood Mirror

**Mood Mirror** is an AI-powered web application that detects your facial emotion from a selfie and provides uplifting suggestions such as happy songs, motivational quotes, and feel-good movies to brighten your mood.

---

## Features

- Detects facial emotions using AI (DeepFace).
- Provides randomized uplifting quotes, songs (with YouTube links), and movies (with IMDb links).
- Simple, user-friendly interface.
- No user data or images are stored.

---

## Technologies Used

- Python 3.x
- Flask (Web framework)
- DeepFace (Emotion detection)
- HTML, CSS, Bootstrap (Frontend)

---

## Installation and Setup

1. Clone the repository:

git clone https://github.com/Gungun525/Mood-Mirror.git
cd Mood-Mirror/MoodMirror

cpp
Copy
Edit

2. (Optional) Create and activate a virtual environment:

python -m venv venv

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

markdown
Copy
Edit

3. Install required Python packages:

pip install -r requirements.txt

markdown
Copy
Edit

4. Run the app:

python app.py

markdown
Copy
Edit

5. Open your browser and visit:

http://127.0.0.1:5000

yaml
Copy
Edit

---

## How It Works

- Upload a selfie.
- The app detects your emotion.
- Randomly displays uplifting quotes, songs, and movies.
- Click on links to enjoy the recommendations.

---

## Project Structure

MoodMirror/
├── app.py
├── templates/
│ └── index.html
├── static/
│ ├── css/
│ └── js/
├── quotes.json
├── songs.json
├── movies.json
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## Future Improvements

- Add webcam live emotion detection.
- More personalized recommendations based on emotion.
- Improved UI/UX.
- Public deployment on cloud.

---

## Credits

- DeepFace library for emotion recognition.
- Flask framework.
- Bootstrap for frontend styling.
- Created by Gungun Kumari.

---

## License

This project is licensed under the MIT License.

---

**Enjoy brightening your day with Mood Mirror!** 😊
