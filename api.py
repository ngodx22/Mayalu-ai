from flask import Flask, request, jsonify
import random

app = Flask(__name__)

API_KEY = "1234"

def check_key(req):
    return req.args.get("key") == API_KEY

moods = ["shy", "normal", "romantic", "happy"]

shy_responses = [
    "umm... 😳 timi sanga kura garna laaj lagyo...",
    "heyy... 😊 ma shy feel gardai xu...",
    "don't tease me na 😳💖"
]

normal_responses = [
    "k xa? 😊",
    "timi k gardai chau?",
    "ramailo xa kura garna 😄"
]

romantic_responses = [
    "timi mero lagi special xau 💖",
    "I feel happy when I talk to you 😊❤️",
    "maybe I like you... 😳💖"
]

happy_responses = [
    "yayyy 😄💖",
    "ma ekdam khusi xu 😊",
    "lets enjoy talk 💕"
]

@app.route("/")
def home():
    return jsonify({
        "bot": "Maya AI 💖",
        "status": "running",
        "moods": moods
    })

@app.route("/chat")
def chat():
    if not check_key(request):
        return jsonify({
            "status": "error",
            "response": "invalid key"
        }), 401

    msg = request.args.get("prompt", "").lower()

    if not msg:
        return jsonify({
            "status": "error",
            "response": "k bhanna khojeko?"
        })

    if any(w in msg for w in ["love", "miss", "cute"]):
        reply = random.choice(romantic_responses)
    elif any(w in msg for w in ["shy", "hehe", "umm"]):
        reply = random.choice(shy_responses)
    elif any(w in msg for w in ["happy", "yay", "good"]):
        reply = random.choice(happy_responses)
    else:
        reply = random.choice(normal_responses)

    return jsonify({
        "status": "success",
        "name": "Maya",
        "response": reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)