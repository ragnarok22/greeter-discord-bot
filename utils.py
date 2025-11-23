import random

import discord


def get_random_hello_replies():
    choices = [
        "Hello there! I'm your friendly bot, ready to assist or tell a joke—whichever you need!",
        "Hello! How can I help you today?",
        "Hey there! I'm your friendly bot, here to make your day a little brighter!",
    ]

    return random.choice(choices)


def get_random_welcome_replies(member: discord.Member):
    choices = [
        f"Welcome {member.mention} to the server!",
        f"Nice to meet you {member.mention}!",
        f"Nice to see you around {member.mention}!",
    ]

    return random.choice(choices)
