import logging
import os
from typing import Optional

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("main")


def get_env(
    key: str, default: Optional[str] = None, required: bool = True
) -> Optional[str]:
    try:
        return os.environ[key]
    except KeyError:
        if required:
            raise Exception(f"Missing environment variable: {key}")
        else:
            return default


token = get_env("DISCORD_API")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
