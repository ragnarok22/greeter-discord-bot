from random import randint

from bot import bot, logger


def generate_random_number(start: int = 0, end: int = 100):
    return randint(start, end)


@bot.command()
async def random(ctx, start: int = 0, end: int = 100):
    logger.info("calling method random")
    number = generate_random_number(start, end)
    await ctx.send(f"The random number is {number}")
