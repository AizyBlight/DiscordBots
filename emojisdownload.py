import discord
from discord.ext import commands
from typing import Union
from config import settings

bot = commands.Bot(command_prefix=settings['PREFIX'], intents=discord.Intents.all())
bot.remove_command('help')

bot.event
async def on_ready():
	print(f'Hello world!')

@bot.command()
async def emoji(ctx, emoji: Union[discord.Emoji, discord.PartialEmoji]):
	embed = discord.Embed(title=f'Name: {emoji.name}', description=f'[Emoji URL]({emoji.url})', color=0x9370DB)
	embed.add_field(name='ID:', value=emoji.id, inline=True)
	embed.set_thumbnail(url=emoji.url)
	await ctx.reply(embed=embed)

bot.run(settings['TOKEN'])