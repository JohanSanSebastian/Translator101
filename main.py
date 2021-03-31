from google_trans_new import google_translator
from langdetect import detect

from discord.ext.commands import Bot
from discord.ext import commands
import discord

from config import token

client = commands.Bot(command_prefix='!')
client.remove_command("help")

translator = google_translator()
client.enabled = True


@client.event
async def on_ready():
    print(f'Bot connected as {client.user}')
    await client.change_presence(activity=discord.Game('Here to connect the community \n !help'))


@client.command()
@commands.has_permissions(ban_members=True)
async def live(ctx):
    stats = 'ON'

    def is_correct(m):
        return m.author.name == ctx.author.name

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

    if client.enabled is True:
        if message.author == client.user:
            return
        
        text = str(message.content)
        lang = translator.detect(text)
        
        if "!t" == text.split()[0]:
            return

        if lang[0] == "en":
            return
        else:
            msg = translator.translate(str(message.content), lang_tgt='en')
            embed = discord.Embed(
                title=msg, description=f"Message in {lang[1]} from {message.author}", color=discord.Color.greyple())
            await message.channel.send(embed=embed)


@client.command()
async def t(ctx, lang, *, message):
    msg = translator.translate(str(message), lang_tgt=lang)
    embed = discord.Embed(
        title=f"Translation to {lang.upper()}", description=msg, color=discord.Color.greyple())
    await ctx.send(embed=embed)


@t.error
async def t_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Invalid language or language not supported")


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

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help", description="All the commands of Translator101", color=0x1bd3f3)
    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/785041781472624664/826870778091274320/discord-avatar-512_1.png?width=369&height=369")
    embed.add_field(name="`!t [language] [text]`",
                    value="To translate any text to any language     ", inline=True)
    embed.add_field(
        name="`!live`", value="To toggle live-translation ON/OFF", inline=True)
    embed.add_field(
        name="`!livestatus`", value="To toggle live-translation ON/OFF", inline=False)
    await ctx.send(embed=embed)


client.run(token)
