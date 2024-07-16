import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()


token = os.getenv('token')
prefix = os.getenv('prefix')

permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True

bot = commands.Bot(prefix, intents=permissoes)

@bot.command()
async def limpar(ctx:commands.Context):
    canal = message.channel.delete
    

@bot.command()
async def ola(ctx:commands.Context):
    usuario = ctx.author
    await ctx.reply(f"Ola, {usuario.display_name}")

@bot.event
async def on_ready():
    print(f"Infelizmente ainda estou vivo...")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send(f"Olá. Sou o {bot.user}")
        
bot.run(token)