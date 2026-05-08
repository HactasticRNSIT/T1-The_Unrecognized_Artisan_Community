from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)

CORS(app)

stories = [
    {
        "title": "Ganesh Chaturthi",
        "story": "Ganesh Chaturthi symbolizes wisdom and unity."
    },
    {
        "title": "Warli Art",
        "story": "Warli art represents harmony with nature."
    },
    {
        "title": "Indian Folk Culture",
        "story": "Indian folk traditions preserve regional identity."
    }
]

@app.route('/')
def home():
    return "CultureVerse AI Backend Running"

@app.route('/story')
def story():
    return jsonify(random.choice(stories))

if __name__ == '__main__':
    app.run(debug=True)
