import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def advice_ecology():
    enxironmental_council = ['Сортировать мусор по разным бакам','Не выкидывать мусор на природу когда вы идёте гулять']
    return random.choice(enxironmental_council)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def advice(ctx):
    await ctx.send(advice_ecology())


@bot.command()
async def ozone_hole(ctx):
    await ctx.send('''Озо́новый слой — часть стратосферы на высоте от 20 до 40 км 
                   Он поглощает часть биологически вредного ультрафиолетового излучения Солнца.
                     Озо́новая дыра́ — это локальное падение концентрации озона в озоновом слое Земли.''')
    
    with open(f'images/unnamed.png' , 'rb') as f:   
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
    
@bot.command()
async def mem_ecology(ctx):
    ecology_mem_img_name = random.choice(os.listdir('mem_ecology'))
    with open(f'mem_ecology/{ecology_mem_img_name}' , 'rb') as f: 
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)    
    
    

bot.run("TOKEN")
