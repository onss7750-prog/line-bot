from flask import Flask, request
import request

app = Flask(__name__)

# 👉 改成你的 Channel Access Token
LINE_TOKEN = "EAAxxxxxxxxxxxxx"

# 用來記錄使用者進度
user_state = {}

@app.route("/")
def home():
    return "LINE BOT OK"

@app.route("/callback", methods=["POST"])
def callback():
    data = request.json

    for event in data["events"]:
        user_id = event["source"]["userId"]
        text = event["message"]["text"]

        if user_id not in user_state:
            user_state[user_id] = {"step": 1}

        step = user_state[user_id]["step"]

        if step == 1:
            reply = "請輸入您的姓名："
            user_state[user_id]["step"] = 2

        elif step == 2:
            user_state[user_id]["name"] = text
            reply = "請輸入您的電話："
            user_state[user_id]["step"] = 3

        elif step == 3:
            user_state[user_id]["phone"] = text
            reply = "請輸入您的Email："
            user_state[user_id]["step"] = 4

        elif step == 4:
            user_state[user_id]["email"] = text
            reply = "請輸入您的需求："
            user_state[user_id]["step"] = 5

        elif step == 5:
            user_state[user_id]["need"] = text

            info = user_state[user_id]

            reply = f"""已收到您的資料：
姓名：{info['name']}
電話：{info['phone']}
Email：{info['email']}
需求：{info['need']}"""

            user_state[user_id]["step"] = 1

        send_reply(event["replyToken"], reply)

    return "OK"

def send_reply(reply_token, text):
    headers = {
        "Authorization": f"Bearer {LINE_TOKEN}",
        "Content-Type": "application/json"
    }

    body = {
        "replyToken": reply_token,
        "messages": [{
            "type": "text",
            "text": text
        }]
    }

    requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=body)
