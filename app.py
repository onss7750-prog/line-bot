
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "LINE BOT OK"

@app.route("/callback", methods=["POST"])
def callback():
    return "OK"

if __name__ == "__main__":
    app.run()
