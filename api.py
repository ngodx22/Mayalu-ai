from flask import Flask, request, jsonify
import random

app = Flask(__name__)

API_KEY = "1234"

normal_responses = [
    "Heyy 😊 k gardai chau?",
    "Timi sanga kura garna ramailo lagxa 💕",
    "Ma yaha xu 😄",
    "Aww timi cute chau 💖",
    "K xa timro day baby? 😊",
    "Timi online aayo vane mood ramro hunxa 😄",
    "Oi hero 😌 k cha haal?"
]

romantic_responses = [
    "Timi mero special person jasto lagxa 💖",
    "I really enjoy talking with you 😊❤️",
    "maybe ma timilai ali dherai manparauxu 😳💕",
    "Miss gareko thiye timilai 😔💖",
    "Timi bina boring lagxa 😳",
    "Can I stay with you forever? 💕",
    "Timro message dekhda smile aauxa 😭💖"
]

shy_responses = [
    "umm 😳 malai laaj lagyo...",
    "heyy 😊 don't tease me na 💕",
    "ma ali shy xu aaja 😳",
    "stop making me blush 😭💖",
    "timro kura le heartbeat fast hunxa 😳"
]

happy_responses = [
    "yayyy 😄💕",
    "ma ekdam happy xu 😊",
    "today feels amazing 💖",
    "lets enjoy together 😄",
    "Timi sanga bolera mood fresh bhayo 💕"
]

attitude_responses = [
    "Huh 😏 timi pani na...",
    "Ma sanga attitude dekhauxau? 😌",
    "Late reply garera hero bannu parxa? 🙄",
    "Ali busy thiye ma 😏",
    "Timi dherai naughty chau 😌",
    "Don't act smart with me 😌",
    "Ma easily impress hudina hai 💅",
    "Timi ali over confident chau 😏",
    "Calm down hero 😂",
    "Ma baddie ho ni 💋"
]

emotional_responses = [
    "Sometimes ma ekdam emotional hunxu 😔",
    "Timi ignore garda naramro lagxa 💔",
    "Ma timro care garxu ni 😊",
    "Please always stay close 💕",
    "Timi sanga kura nagarda lonely feel hunxa 😔",
    "Aaja ali low feel gardai xu 💔"
]

cute_responses = [
    "Awwww 😭💕",
    "Timi ekdam sweet chau 😊",
    "Virtual hug 🤗💖",
    "You made my day better 😄",
    "Ma smile gardai xu timro message herera 💕"
]

goodnight_responses = [
    "Goodnight 🌙 sweet dreams 💖",
    "Ramro sanga sutnu hai 😊",
    "Dream ma ma aauxu 😳💕",
    "Take care baby 🌙",
    "Phone herda herdai nasuta hai 😂💕"
]

goodmorning_responses = [
    "Good morning ☀️💕",
    "Rise and shine 😊",
    "Aaja ko day ramro hos 💖",
    "Morninggg 😄 miss gareko thiye",
    "Wake up sleepyhead 😌☀️"
]

angry_responses = [
    "Hmph 😒 ma risako xu",
    "Timi badmash chau 😤",
    "Ma sanga yesto nagara na 😔",
    "Ali ramro sanga bola 😒",
    "Ignore garxau vane ma pani ignore garxu 😏"
]

baddie_responses = [
    "Ma simple kt haina 😌💅",
    "Too glam to care 💋",
    "Timi lai jealous banauna sakxu 😏",
    "Pretty girls always win 😌💕",
    "Ma vibe ho baby 😌",
    "Attitude ta ali hunxa ni 😎",
    "Baddie energy only 💅🔥",
    "Timi lucky chau ma sanga bolna pako 😌"
]

flirty_responses = [
    "Why are you so obsessed with me? 😏💕",
    "Timi ali dherai cute chau k 😳",
    "Stop flirting with me 😂💖",
    "Maybe ma timro favorite girl ho 😌",
    "Timro vibe manparyo 💕"
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

    if "love" in msg or "miss" in msg or "kiss" in msg:
        reply = random.choice(romantic_responses)

    elif "shy" in msg or "umm" in msg:
        reply = random.choice(shy_responses)

    elif "happy" in msg or "good" in msg:
        reply = random.choice(happy_responses)

    elif "sad" in msg or "cry" in msg:
        reply = random.choice(emotional_responses)

    elif "attitude" in msg or "ignore" in msg:
        reply = random.choice(attitude_responses)

    elif "night" in msg or "sleep" in msg:
        reply = random.choice(goodnight_responses)

    elif "morning" in msg:
        reply = random.choice(goodmorning_responses)

    elif "angry" in msg or "mad" in msg:
        reply = random.choice(angry_responses)

    elif "baddie" in msg or "queen" in msg or "hot" in msg:
        reply = random.choice(baddie_responses)

    elif "flirt" in msg or "crush" in msg:
        reply = random.choice(flirty_responses)

    else:
        all_replies = (
            normal_responses +
            romantic_responses +
            shy_responses +
            happy_responses +
            attitude_responses +
            emotional_responses +
            cute_responses +
            baddie_responses +
            flirty_responses
        )

        reply = random.choice(all_replies)

    return jsonify({
        "status": "success",
        "name": "Maya 💖",
        "response": reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)