import os
import discord
from discord.ext import commands, tasks
import datetime
import asyncio
from keep_alive import keep_alive
import random

intents = discord.Intents.all()
client = commands.Bot(command_prefix='e!', intents=intents, help_command=None)


# notifies us that the bot has run successfully
# sets a listening status on the bot
@client.event
async def on_ready():
  print('good morning, {0.user}!'.format(client))
  await client.change_presence(activity=discord.Activity(
    type=discord.ActivityType.listening, name='e!help'))

# command function to remind a user of a task at a later time
# limitation - cannot take more than one time argument (e.g. e!remindme 1h take a break, but not e!remindme 30s 1h take a break)
@client.command()
async def remindme(ctx, time, *, task):

  # function to convert the user-specified time into seconds
  def convert_time(time):
    # a list of valid time units
    time_units = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600 * 24}

    # get the last character (time unit) from the string
    unit = time[-1]

    # if the specified time unit is not valid, return -1
    if unit not in time_units:
      return -1

    # try to convert the time value to an integer; if it is not a valid int, return -2
    try:
      time_value = int(time[:-1])
    except:
      return -2

    # return the total number of seconds based on the set time
    return time_value * time_units[unit]

  # call the convert_time function to get the number of seconds until the reminder should be sent
  time_in_seconds = convert_time(time)

  # if the time string is not valid, send an error message
  if time_in_seconds == -1 or time_in_seconds == -2:
    await ctx.send(
      'uh oh, please specify a valid time! (｡•́︿•̀｡) \n ⤷   *for example: 1d, 1h, 30m, 10s*'
    )
    return

# send a confirmation message indicating that the reminder has been set
  await ctx.send(embed=discord.Embed(color=0x2f3136,
                                     title='( ｡>︿<) reminder set ⺌',
                                     description=f'{task} in {time}!'))

  # wait for the specified time, and then send a reminder message
  await asyncio.sleep(time_in_seconds)
  await ctx.send(ctx.message.author.mention,
                 embed=discord.Embed(
                   color=0x2f3136,
                   title="(つ .•́ ^ •̀.)づ beep beep! don't forget ⺌",
                   description=f'{task}'))


# command function to say hello to the bot
@client.command()
async def hello(ctx):
  await ctx.send('hello! ₍ᐢ..ᐢ₎')


# command function to check bot ping
@client.command()
async def ping(ctx):
  await ctx.send(f' ⌕ pong! ﹕ {round(client.latency * 1000)}ms')


# command function to show a random gentle reminder
@client.command()
async def gentlereminder(ctx):
  items = [
    discord.Embed(
      colour=0x2f3136,
      title='( ｡>︿<)   gentle reminder  ⺌',
      description=
      'I had a passing thought about whether things will get better, but I realised the answer depends on what I do today'
    ),
    discord.Embed(
      colour=0x2f3136,
      title='( ｡>︿<)   gentle reminder  ⺌',
      description=
      'you are worthy of the time and effort you spend on your needs, wants, and desires. it is okay to take care of yourself regularly, wholeheartedly, and without guilt'
    ),
    discord.Embed(
      colour=0x2f3136,
      title='( ｡>︿<)   gentle reminder  ⺌',
      description=
      'rest is just as important to studying hard when it comes to reaching your goals, and intentional rest is like recharging our batteries so we can return to studying feeling fresh + ready to learn'
    ),
    discord.Embed(
      colour=0x2f3136,
      title='( ｡>︿<)   gentle reminder  ⺌',
      description=
      'in order to become knowledgeable, one must admit ignorance. it is okay not to know something, so do not be discouraged to strive and learn more. that is what learning is about'
    ),
    discord.Embed(
      colour=0x2f3136,
      title='( ｡>︿<)   gentle reminder  ⺌',
      description=
      'asking for help may be a step outside of your comfort zone, but it is also a step toward pursuing your passions, learning something new, becoming more confident, and becoming a better student. thank you for joining better tomorrow - whether it be for finding friends, homework help, or people to study with, I am so proud of you for taking that first step + I wish you all the best.'
    ),
    discord.Embed(colour=0x2f3136,
                  title='( ｡>︿<)   ways to take a break  ⺌',
                  description='stand up + stretch'),
    discord.Embed(colour=0x2f3136,
                  title='( ｡>︿<)   ways to take a break  ⺌',
                  description='get a glass of water'),
    discord.Embed(colour=0x2f3136,
                  title='( ｡>︿<)   ways to take a break  ⺌',
                  description='take a moment to breathe + meditate'),
    discord.Embed(colour=0x2f3136,
                  title='( ｡>︿<)   ways to take a break  ⺌',
                  description='lie down + close your eyes for a bit'),
    discord.Embed(colour=0x2f3136,
                  title='( ｡>︿<)   ways to take a break  ⺌',
                  description='listen to music / a podcast'),
    discord.Embed(colour=0x2f3136,
                  title='( ｡>︿<)   ways to take a break  ⺌',
                  description='have a warm shower'),
    discord.Embed(colour=0x2f3136,
                  title='( ｡>︿<)   ways to take a break  ⺌',
                  description='spend time with a loved one or pet'),
    discord.Embed(colour=0x2f3136,
                  title='( ｡>︿<)   ways to take a break  ⺌',
                  description='go on a walk or sit outside'),
    discord.Embed(colour=0x2f3136,
                  title='( ｡>︿<)   ways to take a break  ⺌',
                  description='have a cup of tea or drink of your choice'),
    discord.Embed(colour=0x2f3136,
                  title='( ｡>︿<)   ways to take a break  ⺌',
                  description='prepare a healthy meal or snack')
  ]
  await ctx.send(embed=random.choice(items))


# command function to send a breathing exercise gif
@client.command()
async def breathe(ctx):
  await ctx.send(
    'https://i.pinimg.com/originals/dc/89/ab/dc89ab18ecf5f62b897aca2d577e3f07.gif'
  )


# command function to show a user guide for eumo
@client.command()
async def help(ctx):
  embed = discord.Embed(
    colour=0x2f3136,
    title='⚘  eumo  ﹕  for studies + work',
    description=
    '↝  enables a user to go into "quiet mode" + hide channels while studying in voice.'
  )
  embed.set_author(
    name='eumo#5077',
    icon_url=
    'https://media.discordapp.net/attachments/1014128857852424233/1095911842217476207/Two_Pears_Icon_Logo.png?width=369&height=369'
  )
  embed.add_field(name='commands',
                  value='`e!help` ﹕ to see a full list of commands',
                  inline=False)
  embed.add_field(name='',
                  value='`e!hello` ﹕ to say hi to eumo!',
                  inline=False)
  embed.add_field(name='',
                  value='`e!ping` ﹕ to get eumos response time',
                  inline=False)
  embed.add_field(name='',
                  value='e!remindme` ﹕ to set reminders',
                  inline=False)
  embed.add_field(name='',
                  value='`e!gentlereminder` ﹕ for kind messages',
                  inline=False)
  embed.add_field(name='', value='`e!breathe` ﹕ for breathing exercises')
  embed.set_footer(text='made with better tomorrow, moi ‎ ♡')
  await ctx.send(embed=embed)


@client.event
async def on_voice_state_update(member: discord.Member, before, after):
  rolelist1 = []
  rolelist2 = []
  print(f'{member} - {after.channel}')
  guild = member.guild

  study_vcs = ['lofi', 'quiet study', 'music study']
  start_roles = ['members']
  end_roles = ['ᶻz  ﹕  quiet mode']

  for i in start_roles:
    rolelist1.append(discord.utils.get(guild.roles, name=i))
  for i in end_roles:
    rolelist2.append(discord.utils.get(guild.roles, name=i))
  if str(after.channel) in study_vcs:

    if not "bots" in [i.name for i in member.roles]:
      for i in rolelist2:
        await member.add_roles(i)
      for i in rolelist1:
        await member.remove_roles(i)

  elif not str(after.channel) in study_vcs:

    if not "bots" in [i.name for i in member.roles]:
      for i in rolelist1:
        await member.add_roles(i)
      for i in rolelist2:
        await member.remove_roles(i)


keep_alive()
client.run(os.getenv('DISCORD_BOT_SECRET'))
