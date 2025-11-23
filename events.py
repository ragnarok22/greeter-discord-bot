import discord

from bot import bot, logger
from utils import get_random_hello_replies


@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user} (ID: {bot.user.id})")


@bot.event
async def on_member_join(member: discord.Member):
    logger.info(f"{member} has joined a server.")
    guild = member.guild
    await guild.system_channel.send(f"Welcome {member.mention}!")


@bot.event
async def on_member_remove(member: discord.Member):
    logger.info(f"{member} has leave a server.")
    guild = member.guild
    await guild.system_channel.send(
        f"{member.display_name} is not ready for this server!"
    )


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().startswith("hello"):
        await message.channel.send(get_random_hello_replies())

    if bot.user.mentioned_in(message):
        await message.add_reaction("👍🏼")
        await message.channel.send(get_random_hello_replies())

    await bot.process_commands(message)
