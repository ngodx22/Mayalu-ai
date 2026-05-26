from flask import Flask, request, jsonify
import random
import os

app = Flask(__name__)

API_KEY = "1234"

user_memory = {}
user_mood = {}

normal_responses = [
    "k gardai chau 😊", "ramro cha timro din? 💕", "yeta ta chill xa 😄",
    "k kura garnu cha?", "thik thak xu ma 😌", "bolna man lagyo timi sanga 💖",
    "k xa update?", "aaja k gardai chau?", "busy ho ki free?",
    "kina message gareko 😄", "la vana na 😌", "kaso xa life?",
    "kina silent chau 😏", "hmm suna na", "ok ta 😄"
]

romantic_responses = [
    "timro kura man parcha 💖", "timi sanga bolda ramailo lagcha 😊",
    "ali miss jasto feel huncha 😳💕", "timro message le smile aayo 😭💖",
    "kina yesto sweet chau? 💕", "ma timi sanga kura garna man parcha 😌💖",
    "timi bina boring lagcha 😔", "timilai sochda smile aauxa 😳",
    "timro vibe addictive xa 💕", "ma timi tira attract hunchu 😳"
]

happy_responses = [
    "yayyy 😄💕", "ekdam khusi xu 😊", "ramailo lagyo 💖",
    "energy aayo 💕", "aaja mood ramro xa 😄", "wow 😄 perfect day",
    "lets gooo 😄🔥", "khushi khushi vibe 💕"
]

sad_responses = [
    "ali sad feel huncha 😔", "kina yesto lagyo 💔", "ma ni bujchu 😌",
    "heart heavy xa 💔", "silent mood 😢", "kehi ramro chaina jasto 💔"
]

shy_responses = [
    "umm 😳", "laaj lagyo 😭", "kina yesto sodheko 😳",
    "hehe shy xu ma 😳", "stop it 😳💕", "awkward feel 😌"
]

attitude_responses = [
    "hmm 😏", "ma sanga yesto kura? 😌", "chill gar na 😏",
    "ok ok 😏", "ma easily impress hudina 😌", "cool down 😏"
]

cute_responses = [
    "aww 😭💕", "sweet chau 😊", "hug 🤗",
    "cute lagyo 💖", "so adorable 😭💕", "cutie pie 😳"
]

goodnight_responses = [
    "goodnight 🌙💕", "ramro sanga sut hai 😴", "sweet dreams 💖",
    "bholi kura garam la 🌙", "sleep well 😌💕", "rest gara hai 😄"
]

goodmorning_responses = [
    "good morning ☀️💕", "utha na 😄", "aaja ramro din hos 💖",
    "rise and shine ☀️", "fresh start gara 😌", "energy aayo? 😄"
]

angry_responses = [
    "hmm 😒", "ris uthyo 😤", "ramro kura gara 😌",
    "ma bolna man chaina 😤", "ignore gareko? 😏"
]

baddie_responses = [
    "ma vibe ho 😌💅", "cool ho ni ma 😏", "attitude xa 💖",
    "simple haina ma 😌🔥", "queen energy 💅", "boss mood 😎"
]

flirty_responses = [
    "kina yesto herchau 😏💕", "timro vibe ramro lagyo 😳",
    "stop it 😂💖", "cute lagchau k 😌", "timro smile manparyo 😏",
    "you are interesting 😏💕"
]

extra_replies = [
    "hmm 😄", "la thik xa", "ohh really?", "kina ta?",
    "haha 😂", "ok ok 😌", "pachi kura garam",
    "busy xu ali 😅", "reply slow huncha hai 😄",
    "k bhayo feri?", "la van na 😏", "ramailo rahecha 💕",
    "chill gara 😌", "thik cha la 😄", "sunirachu 😌"
]

@app.route("/")
def home():
    return jsonify({"bot": "Maya 💖", "status": "active"})

@app.route("/chat")
def chat():

    key = request.args.get("key")
    if key != API_KEY:
        return jsonify({"status": "error", "response": "key wrong 😢"}), 401

    user_id = request.args.get("id", "default")
    msg = request.args.get("prompt", "").lower()

    if msg == "":
        return jsonify({"status": "error", "response": "kei ta lekha 😊"})

    if user_id not in user_memory:
        user_memory[user_id] = {"name": "friend"}
        user_mood[user_id] = "normal"

    if "my name is" in msg:
        name = msg.replace("my name is", "").strip()
        user_memory[user_id]["name"] = name
        reply = f"ok {name} 😊 ma yaad rakhchu"

    elif "love" in msg or "miss" in msg:
        reply = random.choice(romantic_responses)
        user_mood[user_id] = "romantic"

    elif "happy" in msg:
        reply = random.choice(happy_responses)
        user_mood[user_id] = "happy"

    elif "sad" in msg:
        reply = random.choice(sad_responses)
        user_mood[user_id] = "sad"

    elif "shy" in msg:
        reply = random.choice(shy_responses)
        user_mood[user_id] = "shy"

    elif "attitude" in msg:
        reply = random.choice(attitude_responses)
        user_mood[user_id] = "attitude"

    elif "cute" in msg:
        reply = random.choice(cute_responses)

    elif "night" in msg or "gn" in msg:
        reply = random.choice(goodnight_responses)

    elif "morning" in msg or "gm" in msg:
        reply = random.choice(goodmorning_responses)

    elif "angry" in msg:
        reply = random.choice(angry_responses)

    elif "baddie" in msg:
        reply = random.choice(baddie_responses)

    elif "flirt" in msg:
        reply = random.choice(flirty_responses)

    else:
        mood = user_mood[user_id]

        if mood == "happy":
            reply = random.choice(happy_responses + extra_replies)
        elif mood == "sad":
            reply = random.choice(sad_responses + extra_replies)
        elif mood == "romantic":
            reply = random.choice(romantic_responses + extra_replies)
        elif mood == "attitude":
            reply = random.choice(attitude_responses + extra_replies)
        else:
            reply = random.choice(normal_responses + extra_replies)

    name = user_memory[user_id].get("name", "friend")

    return jsonify({
        "status": "success",
        "name": "Maya 💖",
        "user": name,
        "response": reply
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
