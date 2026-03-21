from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "LINE BOT OK"

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    print(body)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
