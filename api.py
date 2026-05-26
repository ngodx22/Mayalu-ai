from flask import Flask, request, jsonify
import random

app = Flask(__name__)

API_KEY = "1234"

normal_responses = [
    "Heyy 😊 k xa timro day?",
    "Timi sanga kura garna ramailo lagxa 💕",
    "Ma yaha xu 😄",
    "Aww timi cute chau 💖"
]

shy_responses = [
    "umm 😳 malai laaj lagyo...",
    "heyy 😊 don't tease me na 💕",
    "ma ali shy xu aaja 😳"
]

romantic_responses = [
    "Timi mero special person jasto lagxa 💖",
    "I really enjoy talking with you 😊❤️",
    "maybe ma timilai ali dherai manparauxu 😳💕"
]

happy_responses = [
    "yayyy 😄💕",
    "ma ekdam happy xu 😊",
    "today feels amazing 💖"
]

@app.route("/")
def home():
    return jsonify({
        "bot": "Maya AI 💖",
        "status": "running",
        "endpoint": "/chat?key=1234&prompt=hello"
    })

@app.route("/chat")
def chat():

    key = request.args.get("key")

    if key != API_KEY:
        return jsonify({
            "status": "error",
            "response": "invalid key 😢"
        }), 401

    msg = request.args.get("prompt", "").lower()

    if msg == "":
        return jsonify({
            "status": "error",
            "response": "kei ta bola 😊"
        })

    if "love" in msg or "miss" in msg or "cute" in msg:
        reply = random.choice(romantic_responses)

    elif "shy" in msg or "umm" in msg or "hehe" in msg:
        reply = random.choice(shy_responses)

    elif "happy" in msg or "yay" in msg or "good" in msg:
        reply = random.choice(happy_responses)

    else:
        reply = random.choice(normal_responses)

    return jsonify({
        "status": "success",
        "name": "Maya 💖",
        "response": reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
