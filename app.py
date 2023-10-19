from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    print("GET /")
    return "Welcome, this is a Flask app deployed on Zeabur"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0')
