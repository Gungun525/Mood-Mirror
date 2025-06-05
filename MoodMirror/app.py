
from flask import Flask, render_template, request
from deepface import DeepFace
import os, random

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

quotes = [
    "Believe you can and you're halfway there.",
    "Every day is a second chance.",
    "You are capable of amazing things.",
    "The best is yet to come.",
    "Happiness looks good on you!"
]

def get_song():
    songs = [
        ("Happy", "Pharrell Williams", "https://youtu.be/ZbZSe6N_BXs"),
        ("Can't Stop The Feeling", "Justin Timberlake", "https://youtu.be/ru0K8uYEZWw"),
        ("Shake It Off", "Taylor Swift", "https://youtu.be/nfWlot6h_JM"),
        ("Good Life", "OneRepublic", "https://youtu.be/q7QQLsC7QEw")
    ]
    return random.choice(songs)

def get_movie():
    movies = [
        ("The Pursuit of Happyness", "2006", "https://www.imdb.com/title/tt0454921/"),
        ("Paddington 2", "2017", "https://www.imdb.com/title/tt4468740/"),
        ("Amélie", "2001", "https://www.imdb.com/title/tt0211915/"),
        ("Up", "2009", "https://www.imdb.com/title/tt1049413/")
    ]
    return random.choice(movies)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    image = request.files['image']
    if image.filename == '':
        return 'No selected file', 400

    if image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)
        try:
            result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
        except Exception as e:
            emotion = "undetected"

        quote = random.choice(quotes)
        song_name, artist, song_link = get_song()
        movie_name, year, movie_link = get_movie()

        os.remove(image_path)  # Deletes uploaded image after use

        return render_template('result.html',
                               emotion=emotion,
                               quote=quote,
                               song_name=song_name,
                               artist=artist,
                               song_link=song_link,
                               movie_name=movie_name,
                               year=year,
                               movie_link=movie_link)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    port = int(os.environ.get("PORT", 5000))  # ✅ This line is key
    app.run(host='0.0.0.0', port=port)        # ✅ This makes it public!

