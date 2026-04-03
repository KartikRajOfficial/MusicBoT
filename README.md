# 🎵 MusicBoT

### Telegram Voice Chat Music Bot (Audio + Video)

<p align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff512f,100:dd2476&height=200&section=header&text=MusicBoT&fontSize=50&fontColor=ffffff&animation=fadeIn"/>

</p>

<p align="center">
<img src="https://img.shields.io/github/stars/KartikRajOfficial/MusicBoT?style=for-the-badge"/>
<img src="https://img.shields.io/github/forks/KartikRajOfficial/MusicBoT?style=for-the-badge"/>
<img src="https://img.shields.io/github/license/KartikRajOfficial/MusicBoT?style=for-the-badge"/>
<img src="https://img.shields.io/github/issues/KartikRajOfficial/MusicBoT?style=for-the-badge"/>
</p>

---

# 🚀 About The Project

**MusicBoT** is a powerful **Telegram Voice Chat Music Bot** that can stream **audio and video directly in Telegram group voice chats**.

It supports **YouTube streaming, queue system, admin controls, and high quality playback**.

Developed by **Kartik Raj** ❤️

---

# ✨ Features

✔ Play music in Telegram voice chats
✔ Supports **YouTube links & search**
✔ Supports **audio + video streaming**
✔ Queue management system
✔ Admin controls
✔ Fast & optimized performance
✔ Easy deployment
✔ Open Source

---

# 🧠 Tech Stack

* Python
* Pyrogram
* PyTgCalls
* FFmpeg
* Docker
* Heroku

---

# 📸 Bot Preview

```
User: /play Believer
Bot: 🎵 Now Playing: Believer
```

---

# 📂 Project Structure

```
MusicBoT
│
├── Kartik/               # Core bot modules
├── strings/              # Bot text messages
│
├── config.py             # Bot configuration
├── requirements.txt      # Python dependencies
├── runtime.txt           # Python runtime
│
├── Dockerfile            # Docker deployment
├── Procfile              # Heroku process
├── heroku.yml            # Heroku config
│
├── sample.env            # Environment variables template
│
├── setup                 # Setup script
├── start                 # Start script
│
└── README.md
```

---

# ⚙️ Environment Variables

Create a `.env` file using `sample.env`.

Example:

```
API_ID=123456
API_HASH=xxxxxxxxxxxxxxxx
BOT_TOKEN=xxxxxxxxxxxxxxxx
SESSION_NAME=MusicBot
SUDO_USERS=123456789
```

---

# 🔑 Required Variables

| Variable     | Description               |
| ------------ | ------------------------- |
| API_ID       | Telegram API ID           |
| API_HASH     | Telegram API Hash         |
| BOT_TOKEN    | Bot Token from BotFather  |
| SESSION_NAME | Pyrogram session          |
| SUDO_USERS   | Telegram User ID of admin |

---

# 💻 Local Installation

### 1 Clone Repository

```
git clone https://github.com/KartikRajOfficial/MusicBoT.git
cd MusicBoT
```

### 2 Install Requirements

```
pip install -r requirements.txt
```

### 3 Setup Environment

Rename

```
sample.env → .env
```

Fill all required variables.

### 4 Run the Bot

```
bash start
```

or

```
python3 -m Kartik
```

---

# ☁️ Deploy

## 🚀 Deploy to Heroku

<p align="center">

<a href="https://heroku.com/deploy">
<img src="https://www.herokucdn.com/deploy/button.svg"/>
</a>

</p>

Steps:

1 Fork the repository
2 Create a Heroku App
3 Connect GitHub repo
4 Add environment variables
5 Deploy

---

## 🚀 Deploy with Docker

Build image

```
docker build . -t musicbot
```

Run container

```
docker run musicbot
```

---

# 🎮 Commands

## General

| Command | Description     |
| ------- | --------------- |
| /start  | Start the bot   |
| /help   | Help menu       |
| /ping   | Check bot speed |

## Music

| Command | Description  |
| ------- | ------------ |
| /play   | Play music   |
| /pause  | Pause music  |
| /resume | Resume music |
| /skip   | Skip song    |
| /stop   | Stop player  |
| /queue  | Show queue   |

---

# 👑 Admin Commands

| Command | Description    |
| ------- | -------------- |
| /mute   | Mute music     |
| /unmute | Unmute         |
| /end    | End voice chat |

---

# 🤝 Contributing

Contributions are welcome!

1 Fork the repo
2 Create a new branch
3 Commit changes
4 Submit pull request

---

# 👨‍💻 Developer

**Kartik Raj**

Founder & Developer

GitHub
https://github.com/KartikRajOfficial

---

# ⭐ Support

If you like this project

⭐ Star the repository
🍴 Fork it
📢 Share with others

---

# 📜 License

This project is licensed under the **MIT License**

---

<p align="center">

Made with ❤️ by **Kartik Raj**

</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff512f,100:dd2476&height=120&section=footer"/>
