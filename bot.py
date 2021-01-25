import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands

#Functrion that get the token {just for privacy}


with open('token.txt' , 'r') as f:
    token = f.readlines()
    
    


#Functions that get the quotes 's price

def get_price(quote_name):
    website = "https://finance.yahoo.com/quote"+ "/" + quote_name + "?" + "p=" + quote_name
    r = requests.get(website)
    soup = BeautifulSoup(r.text , 'lxml')
    div = soup.find('div', class_ = "D(ib) Va(m) Maw(65%) Ov(h)")
    price = div.div.span.text
    return price



# Discord bot

bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def hi(ctx):
    await ctx.send(f'Hello !')

@bot.command()
async def price(ctx, *, stock_name):
    await ctx.send(f'The price of {stock_name} is : {get_price(stock_name)} $')



bot.run(token[0]) #Token is the first line the token.txt file







