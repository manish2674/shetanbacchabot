from flask import Flask, request, render_template
import random

app = Flask(__name__)

rude_replies = [
    "Abe chal na! Kya puch raha hai? 😏",
    "Bohot intelligent ban raha hai? 😎",
    "Mujhe kya? Apne kaam se kaam rakh! 🙄",
    "Bhai, timepass band kar. 😑",
    "Tumhare jaise 100 aaye, 200 gaye! 🤭",
    "Dimaag mat kha, seedha point pe aa! 😈",
    "Shakal dekh apni, phir sawal puch! 😂",
    "Oye, bakwaas band kar! 😒", 
    "Abe chal na! Kya puch raha hai? 😏",
    "Bohot intelligent ban raha hai? 😎",
    "Dimaag mat kharab kar mera! 🤨",
    "Acha? Tere baap ka bot hun kya? 😂",
    "Tumhare liye time nahi hai mere paas! 😈",
    "Teri shakal dekh, phir baat kar! 🤭",
    "Mujhe kya, ja padhai kar! 📚",
    "Bakwas bandh kar! 🤫",
    "Mummy ko bula! 😜"
]

special_replies = {
    "hi": "Hi hi mat kar, kaam bol! 😏",
    "hello": "Hello hello ki zarurat nahi, seedha point pe aa! 😎",
    "bye": "Chal bhag! 😈",
    "thanks": "Shakal dekh apni, thank you bol raha hai! 😂",
    "tuje kisne banaya": "tere papa manish ne!😂😎",
    "mc": "tu khud he bsdke ☺️",
    "bc": "chal chal lodu nikal le gali mat kha abhi abhi bana hu pehla din he mu mat kharab kar🤢"
}

bad_words = ["stupid", "idiot", "mad", "fool", "bakwas", "pagal","chutiya","tmkc","lode","lodu","gand","kutta","useless","mad"]

bad_word_replies = [
    "Apni aukaat me reh! 😎",
    "Mujhe gaali deke khush ho gaya? Baccha hai kya? 😈",
    "tu khud he isiliye mujhe bol raha"
]

def shetan_baccha_bot(user_message):
    msg = user_message.lower()
    for keyword in special_replies:
        if keyword in msg:
            return special_replies[keyword]
    for word in bad_words:
        if word in msg:
            return random.choice(bad_word_replies)
    return random.choice(rude_replies)

@app.route("/", methods=["GET", "POST"])
def home():
    bot_reply = ""
    if request.method == "POST":
        user_message = request.form["message"]
        bot_reply = shetan_baccha_bot(user_message)
    return render_template("index.html", bot_reply=bot_reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
