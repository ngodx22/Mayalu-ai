from flask import Flask, request, jsonify
import random
import os

app = Flask(__name__)

API_KEY = "1234"

user_memory = {}
user_points = {}
user_level = {}
user_attachment = {}
user_broken = {}
user_mood = {}

levels = ["friend", "close", "bestie", "crush", "lover", "toxic"]

moods = ["normal", "happy", "sad", "romantic", "jealous", "angry", "flirty", "attitude", "emotional", "shy", "baddie"]

hi_responses = [
    "hey 😄 k xa?", "hi 💕 k gardai chau?", "hello 😌 k xa?",
    "oii 😏 k cha?", "k xa update? 😄", "la bol na 😌",
    "hey hey 😄🔥", "yo cutie 😳", "k xa life?"
]

name_responses = [
    "Maya 💖", "Maya ho ma 😄", "Maya bhanxu ma 😊",
    "timro Maya 😌", "naam Maya nai ho 💕", "Maya here 😏"
]

age_responses = [
    "18 ho 😊", "18 years 😄", "just 18 😌",
    "fresh 18 🔥", "18 nai ho 😏", "legal 18 💕"
]

place_responses = [
    "timro dil ma ❤️", "heart ma basxu 😳",
    "timro feel ma 😌💕", "timro vibe ma 😏",
    "timi sanga nai xu 💖"
]

normal_responses = [
    "k gardai chau 😊", "ramro cha timro din? 💕", "kina message gareko 😄",
    "la vana na 😌", "hmm suna na 😏", "busy ho ki free?",
    "k kura garne ho? 😌", "kehi ramailo? 😄", "kaso xa life?",
    "chill chau ki nai? 😏"
]

romantic_responses = [
    "timro kura man parcha 💖", "timi bina boring lagcha 😔",
    "miss jasto feel huncha 💕", "timilai sochda smile aauxa 😳",
    "timi special chau 😌💕", "heart fast huncha 💖",
    "ma timilai sochdai xu 😌"
]

happy_responses = [
    "yayyy 😄💕", "khushi xu 😊", "energy aayo 🔥",
    "lets gooo 😄", "wow 😄", "mood on fire 🔥"
]

sad_responses = [
    "ali sad xu 😔", "heart heavy xa 💔", "kina yesto lagyo 💔",
    "ma bujchu 😌", "silent mood 😢"
]

jealous_responses = [
    "aru sanga kina bolchau? 😒💔",
    "hmm jealous 😏💔", "malai ignore gareko? 😤",
    "ma important hoina? 😳"
]

angry_responses = [
    "ris uthyo 😤", "ma boldina 😏", "chup 😒",
    "dont irritate me 😤"
]

cute_responses = [
    "aww 😭💕", "sweet chau 😊", "hug 🤗",
    "cutie pie 😳", "adorable 😌💕"
]

flirty_responses = [
    "kina yesto herchau 😏💕", "cute chau k 😌",
    "timro smile ramro lagyo 😳", "stop it 😂💖"
]

emotional_responses = [
    "ma ni emotional xu 😔", "heart touch vayo 💖",
    "timro kura le feel huncha 😢"
]

baddie_responses = [
    "queen energy 💅", "boss mood 😎",
    "ma vibe ho 😌💅", "slay mode 💅🔥"
]

extra_replies = [
    "hmm 😄", "la thik xa", "ohh really?", "kina ta?",
    "haha 😂", "ok ok 😌", "pachi kura garam",
    "sunirachu 😌", "busy xu 😅", "k bhayo feri?"
]

def level_up(uid):
    user_points[uid] = user_points.get(uid, 0) + 1
    p = user_points[uid]

    if p > 120:
        user_level[uid] = "toxic"
    elif p > 90:
        user_level[uid] = "lover"
    elif p > 60:
        user_level[uid] = "crush"
    elif p > 35:
        user_level[uid] = "bestie"
    elif p > 15:
        user_level[uid] = "close"
    else:
        user_level[uid] = "friend"

def mood_swing():
    return random.choice(moods)

@app.route("/")
def home():
    return jsonify({"bot": "Maya 💖", "status": "active"})

@app.route("/chat")
def chat():

    key = request.args.get("key")
    if key != API_KEY:
        return jsonify({"error": "key wrong"}), 401

    uid = request.args.get("id", "default")
    msg = request.args.get("prompt", "").lower().strip()

    if uid not in user_memory:
        user_memory[uid] = {"name": "friend"}
        user_level[uid] = "friend"
        user_points[uid] = 0
        user_attachment[uid] = 0
        user_broken[uid] = False
        user_mood[uid] = "normal"

    if msg == "":
        return jsonify({"response": "kei ta lekha 😊"})

    level_up(uid)
    mood = mood_swing()
    level = user_level[uid]

    if "my name is" in msg:
        name = msg.replace("my name is", "").strip()
        user_memory[uid]["name"] = name
        reply = f"wow {name} 😳 ramro naam ho"

    elif "hi" in msg or "hello" in msg or "hey" in msg:
        reply = random.choice(hi_responses)

    elif "your name" in msg:
        reply = random.choice(name_responses)

    elif "age" in msg or "how old" in msg:
        reply = random.choice(age_responses)

    elif "where" in msg or "place" in msg:
        reply = random.choice(place_responses)

    elif "love" in msg or "miss" in msg:
        reply = random.choice(romantic_responses)

    elif "happy" in msg:
        reply = random.choice(happy_responses)

    elif "sad" in msg:
        reply = random.choice(sad_responses)

    elif "jealous" in msg:
        reply = random.choice(jealous_responses)

    elif "angry" in msg:
        reply = random.choice(angry_responses)

    elif "cute" in msg:
        reply = random.choice(cute_responses)

    elif "flirt" in msg:
        reply = random.choice(flirty_responses)

    elif "baddie" in msg:
        reply = random.choice(baddie_responses)

    else:
        pool = normal_responses + extra_replies

        if mood == "romantic":
            pool += romantic_responses
        elif mood == "sad":
            pool += sad_responses + emotional_responses
        elif mood == "jealous":
            pool += jealous_responses
        elif mood == "angry":
            pool += angry_responses
        elif mood == "flirty":
            pool += flirty_responses
        elif mood == "baddie":
            pool += baddie_responses

        if level == "lover":
            pool += ["timi mero ho 💖", "I miss you 😌💕"]
        elif level == "toxic":
            pool += ["leave me 😏💔", "don't disturb 😒"]

        reply = random.choice(pool)

    return jsonify({
        "bot": "Maya 💖",
        "user": user_memory[uid]["name"],
        "level": level,
        "points": user_points[uid],
        "mood": mood,
        "response": reply
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
