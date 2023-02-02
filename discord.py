import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="*")  #  Esse é o prefixo de cada comando do bot

@bot.event  #  sempre que acontecer um evento, ele vai fazer alguma coisa
async def on_ready():   #  na hora que estiver pronto, ele vai rodar isso
    print(f"Bot está pronto! Conectado atualmente como {bot.user}")  #  mostrando a id do BOT pra ver se ele conectou

@bot.event
async def on_message(message):  #  evitar que o bot fique falando com ele mesmo
    if message.author == bot.user:
    return


@bot.command(name="oi")  # quando digitar "*oi", ele vai mandar a mensagem abaixo.
async def mandar_ola(ctx):  #  ctx = contexto
    nick = ctx.author.nick  #  autor da postagem
    response = "Olá, " + nick
    await ctx.send(response)


bot.run("")  #  token do bot

