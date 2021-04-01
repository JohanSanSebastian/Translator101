# Importing the necessary translation and language detection libraries
from google_trans_new import google_translator
from langdetect import detect

# Importing all necessary discord.py libraries
from discord.ext.commands import Bot
from discord.ext import commands
import discord

# Importing secret bot token from config.py
from config import token

# Setting up bot
client = commands.Bot(command_prefix='!') # This can be changed to whatever prefix you decide to use for the bot
client.remove_command("help")

# Setting up translator and other required things for the bot
translator = google_translator()
client.enabled = True
client.name = 'Translator101' # This can be changed according to what you decide to name your bot (This will reflect everywhere the name of the bot is mentioned)

@client.event
async def on_ready():
    print(f'Bot connected as {client.user}') # Alert to notify login of bot
    await client.change_presence(activity=discord.Game('Here to connect the community \n !help')) # Setting Rich presence of the bot

# Command to toggle live-translation ON/OFF
@client.command()
@commands.has_permissions(ban_members=True)
async def live(ctx):
    stats = 'ON'

    # Function to check if responses sent in chat is from user who called  the function
    def is_correct(m):
        return m.author.name == ctx.author.name

    # Toggling function
    if client.enabled is False:
        await ctx.send("Would you like to enable live translation? [Yes/No]")

        status = await client.wait_for('message', check=is_correct, timeout=20.0)

        if status.content.lower() == 'yes':
            client.enabled = True
            stats = 'ON'
            await ctx.send(f"Ok I'm going to turn it {stats}")
        else:
            client.enabled = False
            stats = 'OFF'
            await ctx.send(f"Ok I'm going to leave it {stats}")

    else:
        await ctx.send("Would you like to disable live translation? [Yes/No]")

        status = await client.wait_for('message', check=is_correct, timeout=20.0)

        if status.content.lower() == 'no':
            client.enabled = True
            stats = 'ON'
            await ctx.send(f"Ok I'm going to leave it {stats}")
        else:
            client.enabled = False
            stats = 'OFF'
            await ctx.send(f"Ok I'm going to turn it {stats}")


@client.event
async def on_message(message):

    await client.process_commands(message)

    # Checking if live-translation is turned ON to run the live-translation feature
    if client.enabled is True:
        if message.author == client.user:
            return

        text = str(message.content)
        lang = translator.detect(text) # Detecting the language of the text

        if "!t" == text.split()[0]:
            return

        if lang[0] == "en":
            return
        else:
            msg = translator.translate(str(message.content), lang_tgt='en') # Translating the text to English
            embed = discord.Embed(
                title=msg, description=f"Message in {lang[1]} from {message.author}", color=discord.Color.greyple())
            await message.channel.send(embed=embed) # Sending the translation as an embed

# Translation command
@client.command()
async def t(ctx, lang, *, message):
    msg = translator.translate(str(message), lang_tgt=lang)
    embed = discord.Embed(
        title=f"Translation to {lang.upper()}", description=msg, color=discord.Color.greyple())
    await ctx.send(embed=embed)

# Error
@t.error
async def t_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Invalid language or language not supported")

# Command to check status of live-translation
@client.command()
async def livestatus(ctx):
    status = 'ON'
    if client.enabled is True:
        status = 'ON'
    else:
        status = 'OFF'
    embed = discord.Embed(
        title=f"Live-translation Status : {status}", color=discord.Color.blurple())
    await ctx.send(embed=embed)

# Help command
@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help", description=f"All the commands of {client.name}", color=0x1bd3f3)
    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/785041781472624664/826870778091274320/discord-avatar-512_1.png?width=369&height=369")
    embed.add_field(name="`!t [language] [text]`",
                    value="To translate any text to any language     ", inline=True)
    embed.add_field(
        name="`!live`", value="To toggle live-translation ON/OFF", inline=True)
    embed.add_field(
        name="`!livestatus`", value="To toggle live-translation ON/OFF", inline=False)
    await ctx.send(embed=embed)

# Running the bot
client.run(token)
