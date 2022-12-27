from nextcord.ext import commands
from nextcord import Intents
from config import TOKEN
from scraper import get_stats, clear_html_file

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "/", intents=intents)


@bot.command(name="stats")
async def SendMessage(ctx, player:str):

    await ctx.send("Wait 20 seconds")

    result = f"Player:{player}\n\n"
    stats = get_stats(player)

    if "error" in stats.values():
        await ctx.send("Error, probably uncorrect input")
    else:
        for i, (k, v) in enumerate(stats.items()):      #send result
            result += f"{k} : {v} \n"
        await ctx.send(result)
    
    


if __name__ == "__main__":
    bot.run(TOKEN)
