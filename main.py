import os
from discord.ext import commands
import discord

النوايا = discord.Intents.default()
النوايا.message_content = True
النوايا.members = True

البوت = commands.Bot(command_prefix="!", intents=النوايا, help_command=None)


@البوت.event
async def on_ready():
    print(f"تم تشغيل البوت: {البوت.user}")


@البوت.command()
async def بينق(ctx):
    await ctx.send(f"🏓 البينق: {round(البوت.latency * 1000)}ms")


البوت.run("TOKEN")
