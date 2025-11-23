Gretter Discord Bot
===================

Lightweight Discord bot built with `discord.py` that greets members, responds to simple messages, and serves a random-number command.

Features
--------
- Welcomes new members and posts a farewell when they leave.
- Responds with `Hello!` when a user sends `hello`.
- `!random [start] [end]` command sends a random integer (defaults to 0–100).
- Structured logging for easier monitoring.

Requirements
------------
- Python 3.12+
- Discord bot token with **Message Content Intent** and **Server Members Intent** enabled in the Discord Developer Portal.
- Environment variable `DISCORD_API` set to your bot token (a `.env` file is supported).

Quickstart
----------
1) Create and activate a virtual environment
```
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

2) Install dependencies
```
pip install -e .
# or, if you prefer uv:
# uv sync
```

3) Configure your token in `.env`
```
DISCORD_API=your-bot-token-here
```

4) Run the bot
```
python main.py
```

Usage
-----
- Send `hello` in a channel the bot can read to get a quick reply.
- Use `!random` to generate numbers:
  - `!random` → random number 0–100
  - `!random 10 50` → random number between 10 and 50

Project Layout
--------------
- `main.py` – entrypoint that starts the bot.
- `bot.py` – bot setup, intents, logging, and env loading.
- `commands.py` – command implementations (currently `!random`).
- `events.py` – event handlers (ready, member join/leave, message listener).

Notes
-----
- Keep your token secret; never commit your `.env`.
- The bot uses the `!` prefix. Adjust in `bot.py` if you want something else.
- Add more commands by extending `commands.py` and importing them in `main.py`.
