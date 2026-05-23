import requests
import random
from datetime import datetime

BOT_TOKEN = "8382452256:AAGGchwmfh5_LFd8IvWpx68SoD2sWxQ85x8"
CHAT_ID = "7564807530"

messages = [

"""🌅 Good Morning, Warriors!

The best investment you can make is in yourself & your trades! 💹
Today's markets are full of opportunities — don't miss them.

📌 Today's rules:
— Follow signals only
— No emotional trades
— Protect your capital

Rise, grind & profit! 💰🔥""",

"""☀️ Good Morning Champs!

Every green day starts with a disciplined morning. 🏆
Before you touch the platform today:

✅ Set your max loss limit
✅ Check our signals
✅ Clear your mind

Trade with your brain, not your heart! 💡""",

"""🌄 Wakey Wakey, Traders!

"Success is not given. It is earned — on the platform, every single day." 💪

Start today with:
🎯 Focus
🎯 Patience
🎯 Discipline

Our signals are ready. Are YOU? Let's go! 🚀""",

"""🌞 Good Morning, Quotex Family!

Another blessed day to build your financial future! 🙏💰

Remember why you started:
💚 Financial freedom
💚 Better life
💚 Smart income

Stay consistent, follow the channel & let's make it happen! 📈""",

"""☀️ GM Traders!

Slow and steady wins the race in trading. 🐢💨
Don't rush. Don't gamble. Just follow the plan.

Today's mindset:
🧠 One trade at a time
🧠 Risk managed always
🧠 Signals trusted fully

Good morning & good profits ahead! 💸""",

"""🌅 Good Morning, Team!

The traders who win consistently all share ONE habit —
they show up every single day with discipline. 💎

Your morning checklist:
📋 Mindset — calm & focused ✅
📋 Strategy — stick to it ✅
📋 Signals — follow them ✅

Let's have an amazing trading day! 🔥🌟"""

]

photos = [
    "photo1.jpg",
    "photo2.jpg",
    "photo3.jpg",
    "photo4.jpg",
    "photo5.jpg",
    "photo6.jpg"
]

today = datetime.now().day

random.seed(today)

pairs = list(zip(messages, photos))

random.shuffle(pairs)

msg, photo = pairs[0]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

with open(photo, "rb") as img:

    data = {
        "chat_id": CHAT_ID,
        "caption": msg
    }

    files = {
        "photo": img
    }

    response = requests.post(
        url,
        data=data,
        files=files
    )

print(response.json())
