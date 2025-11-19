discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="!")

reminders = []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    check_reminders.start()

@bot.command()
async def remind(ctx, time: int, *, message):
    """!remind 10 اشرب مي -> يذكرك بعد 10 دقائق"""
    reminders.append({"user": ctx.author, "time": time, "message": message})
    await ctx.send(f"تم تسجيل التذكير: {message} بعد {time} دقيقة")

@tasks.loop(seconds=60)
async def check_reminders():
    to_remove = []
    for r in reminders:
        r["time"] -= 1
        if r["time"] <= 0:
            await r["user"].send(f"تذكير: {r['message']}")
            to_remove.append(r)
    for r in to_remove:
        reminders.remove(r)

# ضع هنا التوكن الخاص بالبوت
bot.run("TOKEN_BOT_HERE")
